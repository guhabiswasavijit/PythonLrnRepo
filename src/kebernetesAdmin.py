import subprocess as ps
def _execute_cmd(cmd):

    with ps.Popen(cmd,stdout=ps.PIPE,universal_newlines=True) as process:
        out, err = process.communicate()
        return out