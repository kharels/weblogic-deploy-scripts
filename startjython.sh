# this file is based on the article https://technology.amis.nl/2015/10/04/how-to-use-wlst-as-a-jython-2-7-module/
# please note the changes made to wl.py

. /apps/web/sfw/weblogic/wls-12.1.3.0/wlserver/server/bin/setWLSEnv.sh

export WL_HOME=/apps/web/sfw/weblogic/wls-12.1.3.0/wlserver

export CONFIG_JVM_ARGS=-Djava.security.egd=file:/dev/./urandom 

JYTHON_SEC="-Dweblogic.security.TrustKeyStore=DemoTrust -Dweblogic.security.allowCryptoJDefaultJCEVerification=true -Dweblogic.security.allowCryptoJDefaultPRNG=true -Dweblogic.security.SSL.ignoreHostnameVerification=true"

export PYTHONPATH=.:$WL_HOME/modules/features/weblogic.server.merged:$WL_HOME/server/lib/weblogic.jar:$WL_HOME/comlogic/wls-12.1.3.0/wlserver/common/wlst/lib:$WL_HOME/web/sfw/weblogic/wls-12.1.3.0/oracle_common/common/wlst:/apps/web/sfw/weblogic/wls-12.1t/lib:/apps/web/sfw/weblogic/wls-12.1.3.0/oracle_common/common/wlst/modules:/apps/webserver/common/wlst:$WL_HOME/common/wlst/lib:/apps0/wlserver/common/wlst/modules

/home/share/scripts/jython27/bin/jython $JYTHON_SEC "$@"

exit $?
