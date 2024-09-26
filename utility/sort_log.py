#sorts the content of the log file

def read_logs(path):
    """Read the log file specified by path
    """
    try:
        with open(path, 'r') as log_file:
            log = log_file.readlines()
    
            return log
    except Exception as e:
        print(f"Error : {e}")

def read_categories(log):
    """Orders the log file according to log functionality
    """
    #Debug
    debug = []
    info = []
    errors = []
    misc = []
    for line in log :
        if 'DEBUG' in line:
            debug.append(line)
        elif 'INFO' in line:
            info.append(line)
        elif 'ERROR' in line:
            errors.append(line)
        else:
            misc.append(line)
    return debug, info, errors, misc
            

def order_log(debug, info, errors, misc):
    """orders the log in sequence , INFO->DEBUG->ERRORS->MISC

        Returns:
            Ordered list of logs
    """
    new_log = []
    log_len = len(debug) +len(errors)+len(misc)+len(info)
    
    for line in info:
        new_log.append(line)
    for line in debug:
        new_log.append(line)
    for line in errors:
        new_log.append(line)
    for line in misc:
        new_log.append(line)
        
    print(new_log)
    return new_log

def write_log(path, new_log):
    
    try:
        with open(path, 'w') as new_log_file:
            new_log_file.writelines(new_log)
            return True
    except Exception as e:
        print(f"Error : {e}")
        return False



def main():
    path = 'logs/NM_Wizard_log.txt'
    logs = read_logs(path)
    debug, info , errors, misc = read_categories(logs)
    ordered_log  = order_log(debug,info,errors,misc)
    write_log(path, ordered_log)
    print(f"Sorted logs in {path}")


if __name__ == '__main__':
    main()