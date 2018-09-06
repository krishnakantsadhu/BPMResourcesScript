###################################### Run script ##################################################
## wsadmin.sh -lang jython -user <<user_name>> -password <<password>> -f <<path of script file>>  ##
####################################################################################################

print("==> 1. Creating ... jms/test_as ---------------------")
newact1=AdminTask.createWMQActivationSpec('"WebSphere MQ JMS Provider(cells/PSCell1|resources.xml#builtin_mqprovider)"', '[ -name test_as -jndiName jms/test_as -destinationJndiName jms/test_RQO -destinationType javax.jms.Queue -qmgrName QM1 -wmqTransportType BINDINGS_THEN_CLIENT -qmgrHostname localhost -qmgrPortNumber 1414 -qmgrSvrconnChannel SYSTEM.DEF.SRVCONN]')
AdminTask.modifyWMQActivationSpec(newact1, '-customProperties [[useJNDI true][maxPoolDepth 3]]')
AdminTask.modifyWMQActivationSpec(newact1, '-stopEndpointIfDeliveryFails false')
print("-----------------------------2. Creating ... jms/test1_as ---------------------")
newact2=AdminTask.createWMQActivationSpec('"WebSphere MQ JMS Provider(cells/PSCell1|resources.xml#builtin_mqprovider)"', '[ -name test1_as -jndiName jms/test1_as -destinationJndiName jms/test1_RQO -destinationType javax.jms.Queue -qmgrName QM1 -wmqTransportType BINDINGS_THEN_CLIENT -qmgrHostname localhost -qmgrPortNumber 1414 -qmgrSvrconnChannel SYSTEM.DEF.SRVCONN]')
AdminTask.modifyWMQActivationSpec(newact2, '-customProperties [[useJNDI true][maxPoolDepth 3]]')
AdminTask.modifyWMQActivationSpec(newact2, '-stopEndpointIfDeliveryFails false')
print("-----------------------------3. Creating ... jms/test2_as ---------------------")
newact3=AdminTask.createWMQActivationSpec('"WebSphere MQ JMS Provider(cells/PSCell1|resources.xml#builtin_mqprovider)"', '[ -name test2_as -jndiName jms/test2_as -destinationJndiName jms/test2_RQO -destinationType javax.jms.Queue -qmgrName QM1 -wmqTransportType BINDINGS_THEN_CLIENT -qmgrHostname localhost -qmgrPortNumber 1414 -qmgrSvrconnChannel SYSTEM.DEF.SRVCONN]')
AdminTask.modifyWMQActivationSpec(newact3, '-customProperties [[useJNDI true][maxPoolDepth 3]]')
AdminTask.modifyWMQActivationSpec(newact3, '-stopEndpointIfDeliveryFails false')
print("----------------------------- Save ---------------------------------------------------")
AdminConfig.save()
