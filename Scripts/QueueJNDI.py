
#
#####################################################################
## NOTE: This code is PRELIMINARY, it requires MANUAL VERIFICATION ##
##                    ***********              ******************* ##
#####################################################################
#

import sys
def wsadminToList(inStr):
        outList=[]
        if (len(inStr)>0 and inStr[0]=='[' and inStr[-1]==']'):
                tmpList = inStr[1:-1].split() #splits space-separated lists,
        else:
                tmpList = inStr.split("\n")   #splits for Windows or Linux
        for item in tmpList:
                item = item.rstrip();         #removes any Windows "\r"
                if (len(item)>0):
                        outList.append(item)
        return outList
#endDef

##********************************* Run script ****************************************************##
## wsadmin.sh -lang jacl -user <<user_name>> -password <<password>> -f <<path of script file>>     ##
##****************************************************************************************************##

print "#----------------------------------- Creating testQ1 ------------------------------------------------"
jmsProvider = AdminConfig.getid("/Cell:PSCell1/JMSProvider:WebSphere MQ JMS Provider/" )
template = AdminConfig.listTemplates("MQQueue" )[0]
#?PROBLEM? (jacl 7) previous LINDEX may need variable.split("xx")
name = ["name", "testQ1"]
jndi = ["jndiName", "jms/testQ1"]
queueName = ["baseQueueName", "Q1"]
mqAttrs = [name, jndi, queueName]
queue = AdminConfig.createUsingTemplate("MQQueue", jmsProvider, mqAttrs, template )
AdminConfig.required("J2EEResourceProperty" )
newPropSet = AdminConfig.create("J2EEResourcePropertySet", queue, [] )
propSet = AdminConfig.showAttribute(queue, "propertySet" )
# ------------------------- MDWRITE ---------------------------------------
name = ["name", "MDWRITE"]
required = ["required", "false"]
description = ["description", ""]
value = ["value", "YES"]
rpAttrs = [name, value, description, required]
AdminConfig.create("J2EEResourceProperty", propSet, rpAttrs )
# ------------------------- MDREAD ----------------------------------------
name = ["name", "MDREAD"]
required = ["required", "false"]
description = ["description", ""]
value = ["value", "YES"]
rpAttrs = [name, value, description, required]
AdminConfig.create("J2EEResourceProperty", propSet, rpAttrs )
# ------------------------- MSGBODY ---------------------------------------
name = ["name", "MSGBODY"]
required = ["required", "false"]
description = ["description", ""]
value = ["value", "MQ"]
rpAttrs = [name, value, description, required]
AdminConfig.create("J2EEResourceProperty", propSet, rpAttrs )

# ==========================================================================================================================

print "#----------------------------------- Creating wswe ------------------------------------------------"
jmsProvider = AdminConfig.getid("/Cell:PSCell1/JMSProvider:WebSphere MQ JMS Provider/" )
template = AdminConfig.listTemplates("MQQueue" )[0]
#?PROBLEM? (jacl 42) previous LINDEX may need variable.split("xx")
name = ["name", "wswe"]
jndi = ["jndiName", "jms/testQ2"]
queueName = ["baseQueueName", "Q11"]
mqAttrs = [name, jndi, queueName]
queue = AdminConfig.createUsingTemplate("MQQueue", jmsProvider, mqAttrs, template )
AdminConfig.required("J2EEResourceProperty" )
newPropSet = AdminConfig.create("J2EEResourcePropertySet", queue, [] )
propSet = AdminConfig.showAttribute(queue, "propertySet" )
# ------------------------- MDWRITE ---------------------------------------
name = ["name", "MDWRITE"]
required = ["required", "false"]
description = ["description", ""]
value = ["value", "YES"]
rpAttrs = [name, value, description, required]
AdminConfig.create("J2EEResourceProperty", propSet, rpAttrs )
# ------------------------- MDREAD ----------------------------------------
name = ["name", "MDREAD"]
required = ["required", "false"]
description = ["description", ""]
value = ["value", "YES"]
rpAttrs = [name, value, description, required]
AdminConfig.create("J2EEResourceProperty", propSet, rpAttrs )
# ------------------------- MSGBODY ---------------------------------------
name = ["name", "MSGBODY"]
required = ["required", "false"]
description = ["description", ""]
value = ["value", "MQ"]
rpAttrs = [name, value, description, required]
AdminConfig.create("J2EEResourceProperty", propSet, rpAttrs )

# ==========================================================================================================================

print "#----------------------------------- Creating sdsds ------------------------------------------------"
jmsProvider = AdminConfig.getid("/Cell:PSCell1/JMSProvider:WebSphere MQ JMS Provider/" )
template = AdminConfig.listTemplates("MQQueue" )[0]
#?PROBLEM? (jacl 77) previous LINDEX may need variable.split("xx")
name = ["name", "sdsds"]
jndi = ["jndiName", "jms/testQ3"]
queueName = ["baseQueueName", "Q12"]
mqAttrs = [name, jndi, queueName]
queue = AdminConfig.createUsingTemplate("MQQueue", jmsProvider, mqAttrs, template )
AdminConfig.required("J2EEResourceProperty" )
newPropSet = AdminConfig.create("J2EEResourcePropertySet", queue, [] )
propSet = AdminConfig.showAttribute(queue, "propertySet" )
# ------------------------- MDWRITE ---------------------------------------
name = ["name", "MDWRITE"]
required = ["required", "false"]
description = ["description", ""]
value = ["value", "YES"]
rpAttrs = [name, value, description, required]
AdminConfig.create("J2EEResourceProperty", propSet, rpAttrs )
# ------------------------- MDREAD ----------------------------------------
name = ["name", "MDREAD"]
required = ["required", "false"]
description = ["description", ""]
value = ["value", "YES"]
rpAttrs = [name, value, description, required]
AdminConfig.create("J2EEResourceProperty", propSet, rpAttrs )
# ------------------------- MSGBODY ---------------------------------------
name = ["name", "MSGBODY"]
required = ["required", "false"]
description = ["description", ""]
value = ["value", "MQ"]
rpAttrs = [name, value, description, required]
AdminConfig.create("J2EEResourceProperty", propSet, rpAttrs )

# ==========================================================================================================================

print "#----------------------------------- Creating dsdsdsdsdsd ------------------------------------------------"
jmsProvider = AdminConfig.getid("/Cell:PSCell1/JMSProvider:WebSphere MQ JMS Provider/" )
template = AdminConfig.listTemplates("MQQueue" )[0]
#?PROBLEM? (jacl 112) previous LINDEX may need variable.split("xx")
name = ["name", "dsdsdsdsdsd"]
jndi = ["jndiName", "jms/testQ4"]
queueName = ["baseQueueName", "Q3"]
mqAttrs = [name, jndi, queueName]
queue = AdminConfig.createUsingTemplate("MQQueue", jmsProvider, mqAttrs, template )
AdminConfig.required("J2EEResourceProperty" )
newPropSet = AdminConfig.create("J2EEResourcePropertySet", queue, [] )
propSet = AdminConfig.showAttribute(queue, "propertySet" )
# ------------------------- MDWRITE ---------------------------------------
name = ["name", "MDWRITE"]
required = ["required", "false"]
description = ["description", ""]
value = ["value", "YES"]
rpAttrs = [name, value, description, required]
AdminConfig.create("J2EEResourceProperty", propSet, rpAttrs )
# ------------------------- MDREAD ----------------------------------------
name = ["name", "MDREAD"]
required = ["required", "false"]
description = ["description", ""]
value = ["value", "YES"]
rpAttrs = [name, value, description, required]
AdminConfig.create("J2EEResourceProperty", propSet, rpAttrs )
# ------------------------- MSGBODY ---------------------------------------
name = ["name", "MSGBODY"]
required = ["required", "false"]
description = ["description", ""]
value = ["value", "MQ"]
rpAttrs = [name, value, description, required]
AdminConfig.create("J2EEResourceProperty", propSet, rpAttrs )

# ==========================================================================================================================

print "#----------------------------------- Creating dsdsds ------------------------------------------------"
jmsProvider = AdminConfig.getid("/Cell:PSCell1/JMSProvider:WebSphere MQ JMS Provider/" )
template = AdminConfig.listTemplates("MQQueue" )[0]
#?PROBLEM? (jacl 147) previous LINDEX may need variable.split("xx")
name = ["name", "dsdsds"]
jndi = ["jndiName", "jms/testQ4"]
queueName = ["baseQueueName", "Q3"]
mqAttrs = [name, jndi, queueName]
queue = AdminConfig.createUsingTemplate("MQQueue", jmsProvider, mqAttrs, template )
AdminConfig.required("J2EEResourceProperty" )
newPropSet = AdminConfig.create("J2EEResourcePropertySet", queue, [] )
propSet = AdminConfig.showAttribute(queue, "propertySet" )
# ------------------------- MDWRITE ---------------------------------------
name = ["name", "MDWRITE"]
required = ["required", "false"]
description = ["description", ""]
value = ["value", "YES"]
rpAttrs = [name, value, description, required]
AdminConfig.create("J2EEResourceProperty", propSet, rpAttrs )
# ------------------------- MDREAD ----------------------------------------
name = ["name", "MDREAD"]
required = ["required", "false"]
description = ["description", ""]
value = ["value", "YES"]
rpAttrs = [name, value, description, required]
AdminConfig.create("J2EEResourceProperty", propSet, rpAttrs )
# ------------------------- MSGBODY ---------------------------------------
name = ["name", "MSGBODY"]
required = ["required", "false"]
description = ["description", ""]
value = ["value", "MQ"]
rpAttrs = [name, value, description, required]
AdminConfig.create("J2EEResourceProperty", propSet, rpAttrs )

# ==========================================================================================================================

print "#-----------------------------------Saving the configuration --------------------------------------"
AdminConfig.save( )
print "#-----------------------------------Ending Script------------------------------------------------"
