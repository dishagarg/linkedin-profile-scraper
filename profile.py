# Extracting public profile:
# python profile.py -u http://www.linkedin.com/in/toxtli
#
# Extracting user from a logged in account:
# python profile.py -u http://www.linkedin.com/in/toxtli -c linkedin-config

import sys
import json
import getopt
from LinkedinController import LinkedinController


def main(params):
    config_file = None
    url = None
    opts, args = getopt.getopt(params, "u:c:")
    if opts:
        for o, a in opts:
            if o == "-c":
                config_file = a
            elif o == "-u":
                url = a
    linkedin_tool = LinkedinController(config=config_file, debug=True)
    profile = linkedin_tool.extractProfile(url)
    with open("workfile.json", 'w') as f:
        f.write(json.dumps(profile, sort_keys=True, indent=4, separators=(',', ': ')))

if __name__ == "__main__":
    argv = sys.argv[1:]   # change to be done is here and in linkedin-config.
    # type(argv) is a list
    # print argv ['-u', 'http://'] or ['-u', 'http://', '-c', 'linkedin-config']
    main(argv)
