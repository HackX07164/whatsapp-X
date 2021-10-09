import sys
from setup import HackerModeInstaller

help_msg = """
\033[1mUSAGE:\033[0m
  python3 -B HackerMode/ <command>

\033[1mCOMMANDS:\033[0m
 update   update the tool.
 install  install HackerMode in the system.
 check    check all module and packages. 
 delete   delete the tool from the system.
""".strip()

if __name__ == "__main__":
    HackerMode = HackerModeInstaller()
    if len(sys.argv) > 1:
        try:
            HackerMode.__getattribute__(sys.argv[1])()
        except Exception as e:
            print(e)
    else:
        print(help_msg)