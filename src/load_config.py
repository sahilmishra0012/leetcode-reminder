import configparser

def load_config():

    parser = configparser.ConfigParser()    
    parser.read('/home/samkiller007/leetcode/res/configs/config')   
    
    config_json = {}
    for sect in parser.sections():
        for k,v in parser.items(sect):
            config_json[k] = v
    return config_json