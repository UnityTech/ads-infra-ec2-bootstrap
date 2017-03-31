import json
import os

from shell import shell


#: our package version
__version__ = '1.0.0'

def AWS(snippet):
    """
    Simple AWS CLI helper with json response parsing. For instance js = AWS('s3 ls').
    """
    pid = shell('aws %s' % snippet)
    print '[%s] AWS-CLI (%s) -> "%s"' % ('ok' if pid.code is 0 else 'ko', os.environ['instance'], snippet)
    raw = pid.output(raw=True)
    return None if not raw else json.loads(raw)
