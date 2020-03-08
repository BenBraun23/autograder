from pathlib import Path
from io import StringIO
from abc import ABC, abstractmethod
import sh


# These two cuties make it possible to give partial credit.
# Exit codes  1 - 2, 126 - 165, and 255 have special meaning and should NOT be used
# for anything besides their assigned meaning (1 is usually any exception).
# This is the reason we use exit codes [3, ..., 103], so to calculate student
# score (0 - 100), just add 3 to your calculated score.
RESULTLESS_EXIT_CODE = 0
RESULT_EXIT_CODE_SHIFT = 3  # All exit codes that convey student score are shifted by this
ALLOWED_EXIT_CODES = (RESULTLESS_EXIT_CODE, *range(0 + RESULT_EXIT_CODE_SHIFT, 101 + RESULT_EXIT_CODE_SHIFT))
MAX_RESULT = ALLOWED_EXIT_CODES[-1]
MIN_RESULT = ALLOWED_EXIT_CODES[1]


class TestCase(ABC):
    SUBMISSION_COMPILATION_ARGUMENTS = tuple()  # Extra args you'd like to use during compilation
    COMPILATION_ARGUMENTS = tuple()
    executable_suffix = ".out"               # Default suffix given to the executable
    def __init__(self, path: Path, tests_dir: Path, timeout: int, filter_function):
        self.path = path
        self.timeout = timeout
        self.filter_function = filter_function
        with open(tests_dir / f"output/{path.stem}.txt") as f:
            self.expected_output = self.format_output(f.read())
        with open(tests_dir / f"input/{path.stem}.txt") as f:
            self.input = StringIO(f.read().strip())
        
        # Only really works if test name is in snake_case
        self.name = path.stem.replace("_", " ").capitalize()
    
    def run(self, precompiled_submission: Path):
        """ Returns student score and message to be displayed """
        self.input.seek(0)
        try:
            test_executable = self.compile_testcase(precompiled_submission)
        except sh.ErrorReturnCode as e:
            print(e)
            return 0, "Failed to Compile"
        with StringIO() as runtime_output:
            try:
                result = test_executable(
                    _in=self.input,
                    _out=runtime_output,
                    _timeout=self.timeout,
                    _ok_code=ALLOWED_EXIT_CODES
                )
            except sh.TimeoutException:
                return 0, "Exceeded Time Limit"
            except sh.ErrorReturnCode as e:
                return 0, "Crashed"
            if result.exit_code != RESULTLESS_EXIT_CODE:
                score = result.exit_code - RESULT_EXIT_CODE_SHIFT
                return score, f"{score}/100"
            elif self.format_output(runtime_output.getvalue()) == self.expected_output:
                return 100, "100/100"
            else:
                return 0, "Wrong answer"
    
    def make_executable_path(self, submission: Path):
        """ By combining test name and student name, it makes a unique path """
        return self.path.with_name(self.path.stem + submission.stem + self.executable_suffix)
    
    def format_output(self, output: str):
        """ Removes whitespace and normalizes the output """
        return "".join(filter(self.filter_function, "".join(output.lower().split())))
    
    @classmethod
    def precompile_submission(cls, submission: Path) -> Path:
        """ Either precompiles student submission and returns the path to
            the precompiled submission or to original submission if no
            precompilation is necesessary
        """
        return submission

    @abstractmethod
    def compile_testcase(self, precompiled_submission: Path) -> sh.Command:
        """ Either precompiles student submission and returns the path to
            the precompiled submission or to original submission if no
            precompilation is necesessary
        """
        pass


class CTestCase(TestCase):
    source_suffix = ".c"
    SUBMISSION_COMPILATION_ARGS = ("-Dscanf_s=scanf", "-Dmain=__student_main__")
    COMPILATION_ARGS = (
        f"-DNO_RESULT={RESULTLESS_EXIT_CODE}",
        f"-DRESULT(x)=x+({RESULT_EXIT_CODE_SHIFT})",
        f"-DPASS={MAX_RESULT}",
        f"-DFAIL={MIN_RESULT}"
    )

    @classmethod
    def precompile_submission(cls, submission: Path) -> Path:
        """ Links student submission without compiling it.
            It is done to speed up total compilation time
        """
        sh.gcc("-c", f"{submission.name}", *cls.SUBMISSION_COMPILATION_ARGS)
        return submission.with_suffix(".o")

    def compile_testcase(self, precompiled_submission: Path) -> sh.Command:
        executable_path = self.make_executable_path(precompiled_submission)
        sh.gcc(
            "-o",
            executable_path,
            self.path,
            precompiled_submission.name,
            *self.COMPILATION_ARGS
        )
        return sh.Command(executable_path)


class JavaTestCase(TestCase):
    """ Please, ask students to remove their main as it could generate errors """
    source_suffix = ".java"

    def compile_testcase(self, precompiled_submission: Path) -> sh.Command:
        sh.javac(self.path, precompiled_submission.name)
        return lambda **kwargs: sh.java(self.path.stem, **kwargs)