
"""
Module to expose more detailed version info for the installed `scipy`
"""
version = "1.18.1"
full_version = version
short_version = version.split('.dev')[0]
git_revision = "e4e854eaa8f18d807cd3496028e257e36caa93cc"
release = 'dev' not in version and '+' not in version

if not release:
    version = full_version
