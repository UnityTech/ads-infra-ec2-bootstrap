import glob
import json
import os

from shell import shell

if __name__ == '__main__':
    
    #
    # - grab the EC2 instance metadata
    # - fetch the instance ID and region (required for the subsequent calls to the AWS CLI)
    #
    raw = shell('wget -q -O - http://169.254.169.254/latest/dynamic/instance-identity/document/').output()
    assert raw
    
    #
    # - parse for UTF8 json
    # 
    js = json.loads(''.join(raw))
    assert js

    #
    # - cherry pick a few interesting quantities
    # - set as env. variables
    # - glob the mounted ./scripts directory for *.py files
    # - exec each and pipe both stdout + stderr
    #
    os.environ['region'] = js['region']
    os.environ['instance'] = js['instanceId']
    matches = glob.glob('scripts/*.py')
    print 'found %d script(s) to run' % len(matches)
    for match in matches:
        pid = shell('/usr/bin/python %s' % match)
        assert pid
        print 'executing %s (exit %d) ->\n  %s' % (match, pid.code, '\n  '.join(pid.output() + pid.errors()))
 