import sys

#---------------------------------------------------------------------
# MAIN FUNCTION
#---------------------------------------------------------------------
def main():
    try:
        with open('pyWords.ini', "r+", encoding = 'windows-1251') as fd:
            for buf in fd:
                try:
                    # buf, _ = buf.split('\n') # for last string in file
                    # buf.replace("\n", "")
                    lines = buf.splitlines()
                except ValueError as err:
                    pass
                arr = lines[0].split("=")
                print(arr[0], '=', arr[1])
    except FileNotFoundError as err:            
        print(err)
        return None
    else:
        pass

#---------------------------------------------------------------------
# RUN MAIN FUNCTION
#---------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(main())
