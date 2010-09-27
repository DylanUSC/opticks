import os
import os.path
import SCons.Warnings

class QwtNotFound(SCons.Warnings.Warning):
    pass
SCons.Warnings.enableWarningClass(QwtNotFound)

def generate(env):
    path = os.environ.get('OPTICKSDEPENDENCIES',None)
    if path:
       path = os.path.join(path, "qwt")
    if not path:
       SCons.Warnings.warn(QwtNotFound,"Could not detect Qwt")
    else:
       qtpath = os.environ.get('OPTICKSDEPENDENCIES',None)
       if qtpath:
          qtpath = os.path.join(qtpath, "Qt")
       if not qtpath:
          SCons.Warnings.warn(QwtNotFound,"Could not detect Qt")
       else:
          libpath = '%s/lib/%s' % (path,env["OPTICKSPLATFORM"])
          lib = "qwt"
          include_platform = env["OPTICKSPLATFORM"]
          if env["OS"] == "windows":
             libpath = '%s/lib/%s/%s' % (path,env["OPTICKSPLATFORM"],env["MODE"])
             lib = "qwt5"
             include_platform = env["OS"]
          env.AppendUnique(CXXFLAGS=["-I%s/include" % (path), "-I%s/include/%s/QtCore" % (qtpath,include_platform), "-I%s/include/%s/QtGui" % (qtpath,include_platform)],
                           LIBPATH=libpath,
                           LIBS=[lib])

def exists(env):
    return env.Detect('qwt')
