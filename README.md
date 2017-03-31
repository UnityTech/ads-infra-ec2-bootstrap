## Mini AWS CLI / Python tooling container 

### Overview

This container is a small proxy to the AWS CLI plus a trivial [**Python**](https://www.python.org/) package 
containing some boilerplate tools. Any python module found under the local script folder will be executed and
have a few basic EC2 quantities passed as enviroment variables (typically the region or instance id). In addition
a handy wrapper to invoke/parse calls to the AWS API is available.

No more messy AWS CLI install plus freedom to script your boot sequence! Please note The instance running this
container **must have a proper IAM role** allowing whatever AWS API calls are specified in the python scripts (e.g
there are no AWS credentials passed to the container). The container is meant to be used as a tool, e.g via a one-shot
docker run.

### Example

Simply create or copy over Python scripts and run the container mounting your script directory to
*/home/local/scripts*, for instance:

```
$ cat > foo.py <<-EOM
> from bootstrap import AWS
> js = AWS('s3 ls')
> print 'found %d S3 entries' % len(js)
>EOM
$ docker run -it -v $(pwd):/home/local/scripts ads-infra-ec2-bootstrap
executing scripts/foo.py (exit 0) ->
  [ok] AWS-CLI (i-0ff68e06b9771448c) -> "s3 ls"
  found 10 S3 entries
```

### Support

Contact olivierp@unity3d.com for more information about this project.