############################# BPM Resource generation script #################################################
## Author  : Krishnakant                                                                                    ##
## Version : 1.0                                                                                            ##
## Date    : Thu Sep 06 15:13:25 IST 2018                                                                   ##
## Usage   : wsadmin.sh -lang jython -user <<user_name>> -password <<password>> -f <<path of script file>>  ##
##############################################################################################################



#-----------------------------------------------------------------------------
# init
#-----------------------------------------------------------------------------
isSkipIfExist = 1
cellName = AdminControl.getCell()
cellID = '/Cell:%s'%cellName
scopeID = AdminConfig.getid(cellID)
queues = AdminConfig.list('MQQueue',scopeID).splitlines()
connectionFactories = AdminConfig.list( 'MQQueueConnectionFactory', scopeID ).splitlines()
activationSpecs =  AdminConfig.list( 'J2CActivationSpec', scopeID ).splitlines()
GREEN = '[92m'
YELLOW = '[93m'
RED = '[91m'
END = '[0m'
#-----------------------------------------------------------------------------
# ----------------------- Activation Spec  DOX_CHNGPRICEPLAN_WRITE_AP1_AS_SCRM------------------------------------------------------
activationSpecName = 'jms/DOX_CHNGPRICEPLAN_WRITE_AP1_AS_SCRM'
asAttrs = '-name DOX_CHNGPRICEPLAN_WRITE_AP1_AS_SCRM -jndiName jms/DOX_CHNGPRICEPLAN_WRITE_AP1_AS_SCRM -destinationJndiName jms/DOX_CHNGPRICEPLAN_WRITE_RPO_SCRM -qmgrName QMEIBAU1 '
asAttrs += '-wmqTransportType BINDINGS_THEN_CLIENT -qmgrHostname 10.87.205.69 -qmgrPortNumber 5433 -qmgrSvrconnChannel SYSTEM.DEF.SRVCONN '
asAttrs += '-stopEndpointIfDeliveryFails false -customProperties [[useJNDI true][maxPoolDepth 3]] -destinationType javax.jms.Queue'
isExist = 1
for asId in activationSpecs:
	if AdminConfig.showAttribute( asId, 'jndiName' ) == activationSpecName:
		print '[Waring] : Activation Specification (%s) %salready Exist%s'%(activationSpecName,YELLOW,END)
		if isSkipIfExist == 1:
			echoMessage = '[Warning] : %sDeleting%s Activation Specification (%s)'% (RED,END,activationSpecName)
			print echoMessage,
			AdminTask.deleteWMQActivationSpec(asId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Activation Specification (%s)'% (YELLOW,END,activationSpecName)
			isExist = 0
		break
if isExist == 1:
	echoMessage = '[Info] : Creating Activation Specification (%s)'% activationSpecName
	print echoMessage,
	done = AdminTask.createWMQActivationSpec( scopeID, asAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()

# ----------------------- Activation Spec  DOX_CHNGBIILINGARRANGEMENT_WRITE_AP1_AS_SCRM------------------------------------------------------
activationSpecName = 'jms/DOX_CHNGBIILINGARRANGEMENT_WRITE_AP1_AS_SCRM'
asAttrs = '-name DOX_CHNGBIILINGARRANGEMENT_WRITE_AP1_AS_SCRM -jndiName jms/DOX_CHNGBIILINGARRANGEMENT_WRITE_AP1_AS_SCRM -destinationJndiName jms/DOX_CHNGBIILINGARRANGEMENT_WRITE_RPO_SCRM -qmgrName QMEIBAU1 '
asAttrs += '-wmqTransportType BINDINGS_THEN_CLIENT -qmgrHostname 10.87.205.69 -qmgrPortNumber 5433 -qmgrSvrconnChannel SYSTEM.DEF.SRVCONN '
asAttrs += '-stopEndpointIfDeliveryFails false -customProperties [[useJNDI true][maxPoolDepth 3]] -destinationType javax.jms.Queue'
isExist = 1
for asId in activationSpecs:
	if AdminConfig.showAttribute( asId, 'jndiName' ) == activationSpecName:
		print '[Waring] : Activation Specification (%s) %salready Exist%s'%(activationSpecName,YELLOW,END)
		if isSkipIfExist == 1:
			echoMessage = '[Warning] : %sDeleting%s Activation Specification (%s)'% (RED,END,activationSpecName)
			print echoMessage,
			AdminTask.deleteWMQActivationSpec(asId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Activation Specification (%s)'% (YELLOW,END,activationSpecName)
			isExist = 0
		break
if isExist == 1:
	echoMessage = '[Info] : Creating Activation Specification (%s)'% activationSpecName
	print echoMessage,
	done = AdminTask.createWMQActivationSpec( scopeID, asAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()

# ----------------------- Activation Spec  DOX_MVSUBSCRIBER_WRITE_AP1_AS_SCRM------------------------------------------------------
activationSpecName = 'jms/DOX_MVSUBSCRIBER_WRITE_AP1_AS_SCRM'
asAttrs = '-name DOX_MVSUBSCRIBER_WRITE_AP1_AS_SCRM -jndiName jms/DOX_MVSUBSCRIBER_WRITE_AP1_AS_SCRM -destinationJndiName jms/DOX_MVSUBSCRIBER_WRITE_RPO_SCRM -qmgrName QMEIBAU1 '
asAttrs += '-wmqTransportType BINDINGS_THEN_CLIENT -qmgrHostname 10.87.205.69 -qmgrPortNumber 5433 -qmgrSvrconnChannel SYSTEM.DEF.SRVCONN '
asAttrs += '-stopEndpointIfDeliveryFails false -customProperties [[useJNDI true][maxPoolDepth 3]] -destinationType javax.jms.Queue'
isExist = 1
for asId in activationSpecs:
	if AdminConfig.showAttribute( asId, 'jndiName' ) == activationSpecName:
		print '[Waring] : Activation Specification (%s) %salready Exist%s'%(activationSpecName,YELLOW,END)
		if isSkipIfExist == 1:
			echoMessage = '[Warning] : %sDeleting%s Activation Specification (%s)'% (RED,END,activationSpecName)
			print echoMessage,
			AdminTask.deleteWMQActivationSpec(asId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Activation Specification (%s)'% (YELLOW,END,activationSpecName)
			isExist = 0
		break
if isExist == 1:
	echoMessage = '[Info] : Creating Activation Specification (%s)'% activationSpecName
	print echoMessage,
	done = AdminTask.createWMQActivationSpec( scopeID, asAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()

# ----------------------- Activation Spec  DOX_SEARCHENTITY_READ_RPO_AS_SCRM------------------------------------------------------
activationSpecName = 'jms/DOX_SEARCHENTITY_READ_RPO_AS_SCRM'
asAttrs = '-name DOX_SEARCHENTITY_READ_RPO_AS_SCRM -jndiName jms/DOX_SEARCHENTITY_READ_RPO_AS_SCRM -destinationJndiName jms/DOX_SEARCHENTITY_READ_RPO_SCRM -qmgrName QMEIBAU1 '
asAttrs += '-wmqTransportType BINDINGS_THEN_CLIENT -qmgrHostname 10.87.205.69 -qmgrPortNumber 5433 -qmgrSvrconnChannel SYSTEM.DEF.SRVCONN '
asAttrs += '-stopEndpointIfDeliveryFails false -customProperties [[useJNDI true][maxPoolDepth 3]] -destinationType javax.jms.Queue'
isExist = 1
for asId in activationSpecs:
	if AdminConfig.showAttribute( asId, 'jndiName' ) == activationSpecName:
		print '[Waring] : Activation Specification (%s) %salready Exist%s'%(activationSpecName,YELLOW,END)
		if isSkipIfExist == 1:
			echoMessage = '[Warning] : %sDeleting%s Activation Specification (%s)'% (RED,END,activationSpecName)
			print echoMessage,
			AdminTask.deleteWMQActivationSpec(asId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Activation Specification (%s)'% (YELLOW,END,activationSpecName)
			isExist = 0
		break
if isExist == 1:
	echoMessage = '[Info] : Creating Activation Specification (%s)'% activationSpecName
	print echoMessage,
	done = AdminTask.createWMQActivationSpec( scopeID, asAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()

# ----------------------- Activation Spec  DOX_GETAGREEMENTINFO_READ_AP1_AS_SCRM------------------------------------------------------
activationSpecName = 'jms/DOX_GETAGREEMENTINFO_READ_AP1_AS_SCRM'
asAttrs = '-name DOX_GETAGREEMENTINFO_READ_AP1_AS_SCRM -jndiName jms/DOX_GETAGREEMENTINFO_READ_AP1_AS_SCRM -destinationJndiName jms/DOX_GETAGREEMENTINFO_READ_RPO_SCRM -qmgrName QMEIBAU1 '
asAttrs += '-wmqTransportType BINDINGS_THEN_CLIENT -qmgrHostname 10.87.205.69 -qmgrPortNumber 5433 -qmgrSvrconnChannel SYSTEM.DEF.SRVCONN '
asAttrs += '-stopEndpointIfDeliveryFails false -customProperties [[useJNDI true][maxPoolDepth 3]] -destinationType javax.jms.Queue'
isExist = 1
for asId in activationSpecs:
	if AdminConfig.showAttribute( asId, 'jndiName' ) == activationSpecName:
		print '[Waring] : Activation Specification (%s) %salready Exist%s'%(activationSpecName,YELLOW,END)
		if isSkipIfExist == 1:
			echoMessage = '[Warning] : %sDeleting%s Activation Specification (%s)'% (RED,END,activationSpecName)
			print echoMessage,
			AdminTask.deleteWMQActivationSpec(asId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Activation Specification (%s)'% (YELLOW,END,activationSpecName)
			isExist = 0
		break
if isExist == 1:
	echoMessage = '[Info] : Creating Activation Specification (%s)'% activationSpecName
	print echoMessage,
	done = AdminTask.createWMQActivationSpec( scopeID, asAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()

# ----------------------- Activation Spec  DOX_GETBILLINGARRANGEMENT_READ_AP1_AS_SCRM------------------------------------------------------
activationSpecName = 'jms/DOX_GETBILLINGARRANGEMENT_READ_AP1_AS_SCRM'
asAttrs = '-name DOX_GETBILLINGARRANGEMENT_READ_AP1_AS_SCRM -jndiName jms/DOX_GETBILLINGARRANGEMENT_READ_AP1_AS_SCRM -destinationJndiName jms/DOX_GETBILLINGARRANGEMENT_READ_RPO_SCRM -qmgrName QMEIBAU1 '
asAttrs += '-wmqTransportType BINDINGS_THEN_CLIENT -qmgrHostname 10.87.205.69 -qmgrPortNumber 5433 -qmgrSvrconnChannel SYSTEM.DEF.SRVCONN '
asAttrs += '-stopEndpointIfDeliveryFails false -customProperties [[useJNDI true][maxPoolDepth 3]] -destinationType javax.jms.Queue'
isExist = 1
for asId in activationSpecs:
	if AdminConfig.showAttribute( asId, 'jndiName' ) == activationSpecName:
		print '[Waring] : Activation Specification (%s) %salready Exist%s'%(activationSpecName,YELLOW,END)
		if isSkipIfExist == 1:
			echoMessage = '[Warning] : %sDeleting%s Activation Specification (%s)'% (RED,END,activationSpecName)
			print echoMessage,
			AdminTask.deleteWMQActivationSpec(asId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Activation Specification (%s)'% (YELLOW,END,activationSpecName)
			isExist = 0
		break
if isExist == 1:
	echoMessage = '[Info] : Creating Activation Specification (%s)'% activationSpecName
	print echoMessage,
	done = AdminTask.createWMQActivationSpec( scopeID, asAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()

# ----------------------- Activation Spec  DOX_PARENTINFO_READ_AP1_AS_SCRM------------------------------------------------------
activationSpecName = 'jms/DOX_PARENTINFO_READ_AP1_AS_SCRM'
asAttrs = '-name DOX_PARENTINFO_READ_AP1_AS_SCRM -jndiName jms/DOX_PARENTINFO_READ_AP1_AS_SCRM -destinationJndiName jms/DOX_PARENTINFO_READ_RPO_SCRM -qmgrName QMEIBAU1 '
asAttrs += '-wmqTransportType BINDINGS_THEN_CLIENT -qmgrHostname 10.87.205.69 -qmgrPortNumber 5433 -qmgrSvrconnChannel SYSTEM.DEF.SRVCONN '
asAttrs += '-stopEndpointIfDeliveryFails false -customProperties [[useJNDI true][maxPoolDepth 3]] -destinationType javax.jms.Queue'
isExist = 1
for asId in activationSpecs:
	if AdminConfig.showAttribute( asId, 'jndiName' ) == activationSpecName:
		print '[Waring] : Activation Specification (%s) %salready Exist%s'%(activationSpecName,YELLOW,END)
		if isSkipIfExist == 1:
			echoMessage = '[Warning] : %sDeleting%s Activation Specification (%s)'% (RED,END,activationSpecName)
			print echoMessage,
			AdminTask.deleteWMQActivationSpec(asId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Activation Specification (%s)'% (YELLOW,END,activationSpecName)
			isExist = 0
		break
if isExist == 1:
	echoMessage = '[Info] : Creating Activation Specification (%s)'% activationSpecName
	print echoMessage,
	done = AdminTask.createWMQActivationSpec( scopeID, asAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()

# ----------------------- Activation Spec  DOX_UPDATEAGREEMENT_READ_AP1_AS_SCRM------------------------------------------------------
activationSpecName = 'jms/DOX_UPDATEAGREEMENT_READ_AP1_AS_SCRM'
asAttrs = '-name DOX_UPDATEAGREEMENT_READ_AP1_AS_SCRM -jndiName jms/DOX_UPDATEAGREEMENT_READ_AP1_AS_SCRM -destinationJndiName jms/DOX_UPDATEAGREEMENT_READ_RPO_SCRM -qmgrName QMEIBAU1 '
asAttrs += '-wmqTransportType BINDINGS_THEN_CLIENT -qmgrHostname 10.87.205.69 -qmgrPortNumber 5433 -qmgrSvrconnChannel SYSTEM.DEF.SRVCONN '
asAttrs += '-stopEndpointIfDeliveryFails false -customProperties [[useJNDI true][maxPoolDepth 3]] -destinationType javax.jms.Queue'
isExist = 1
for asId in activationSpecs:
	if AdminConfig.showAttribute( asId, 'jndiName' ) == activationSpecName:
		print '[Waring] : Activation Specification (%s) %salready Exist%s'%(activationSpecName,YELLOW,END)
		if isSkipIfExist == 1:
			echoMessage = '[Warning] : %sDeleting%s Activation Specification (%s)'% (RED,END,activationSpecName)
			print echoMessage,
			AdminTask.deleteWMQActivationSpec(asId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Activation Specification (%s)'% (YELLOW,END,activationSpecName)
			isExist = 0
		break
if isExist == 1:
	echoMessage = '[Info] : Creating Activation Specification (%s)'% activationSpecName
	print echoMessage,
	done = AdminTask.createWMQActivationSpec( scopeID, asAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()

# ----------------------- Activation Spec  EAIToBPMREDPESubOfferReceiveAS_SCRM------------------------------------------------------
activationSpecName = 'jms/EAIToBPMREDPESubOfferReceiveAS_SCRM'
asAttrs = '-name EAIToBPMREDPESubOfferReceiveAS_SCRM -jndiName jms/EAIToBPMREDPESubOfferReceiveAS_SCRM -destinationJndiName jms/EAIToBPMREDPESubOfferReceiveQ_SCRM -qmgrName QMEIBAU1 '
asAttrs += '-wmqTransportType BINDINGS_THEN_CLIENT -qmgrHostname 10.87.205.69 -qmgrPortNumber 5433 -qmgrSvrconnChannel SYSTEM.DEF.SRVCONN '
asAttrs += '-stopEndpointIfDeliveryFails false -customProperties [[useJNDI true][maxPoolDepth 3]] -destinationType javax.jms.Queue'
isExist = 1
for asId in activationSpecs:
	if AdminConfig.showAttribute( asId, 'jndiName' ) == activationSpecName:
		print '[Waring] : Activation Specification (%s) %salready Exist%s'%(activationSpecName,YELLOW,END)
		if isSkipIfExist == 1:
			echoMessage = '[Warning] : %sDeleting%s Activation Specification (%s)'% (RED,END,activationSpecName)
			print echoMessage,
			AdminTask.deleteWMQActivationSpec(asId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Activation Specification (%s)'% (YELLOW,END,activationSpecName)
			isExist = 0
		break
if isExist == 1:
	echoMessage = '[Info] : Creating Activation Specification (%s)'% activationSpecName
	print echoMessage,
	done = AdminTask.createWMQActivationSpec( scopeID, asAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()

# ----------------------- Activation Spec  WPStoEAIRECCDELQueueAS_SCRM------------------------------------------------------
activationSpecName = 'jms/WPStoEAIRECCDELQueueAS_SCRM'
asAttrs = '-name WPStoEAIRECCDELQueueAS_SCRM -jndiName jms/WPStoEAIRECCDELQueueAS_SCRM -destinationJndiName jms/EAItoWPSRECCDELReceiveQueue_SCRM -qmgrName QMEIBAU1 '
asAttrs += '-wmqTransportType BINDINGS_THEN_CLIENT -qmgrHostname 10.87.205.69 -qmgrPortNumber 5433 -qmgrSvrconnChannel SYSTEM.DEF.SRVCONN '
asAttrs += '-stopEndpointIfDeliveryFails false -customProperties [[useJNDI true][maxPoolDepth 3]] -destinationType javax.jms.Queue'
isExist = 1
for asId in activationSpecs:
	if AdminConfig.showAttribute( asId, 'jndiName' ) == activationSpecName:
		print '[Waring] : Activation Specification (%s) %salready Exist%s'%(activationSpecName,YELLOW,END)
		if isSkipIfExist == 1:
			echoMessage = '[Warning] : %sDeleting%s Activation Specification (%s)'% (RED,END,activationSpecName)
			print echoMessage,
			AdminTask.deleteWMQActivationSpec(asId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Activation Specification (%s)'% (YELLOW,END,activationSpecName)
			isExist = 0
		break
if isExist == 1:
	echoMessage = '[Info] : Creating Activation Specification (%s)'% activationSpecName
	print echoMessage,
	done = AdminTask.createWMQActivationSpec( scopeID, asAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()

# ----------------------- Activation Spec  REDPLUSToRECCAdapterQAS_SCRM------------------------------------------------------
activationSpecName = 'jms/REDPLUSToRECCAdapterQAS_SCRM'
asAttrs = '-name REDPLUSToRECCAdapterQAS_SCRM -jndiName jms/REDPLUSToRECCAdapterQAS_SCRM -destinationJndiName jms/EAItoAdapterRECCReceiveQueue_SCRM -qmgrName QMEIBAU1 '
asAttrs += '-wmqTransportType BINDINGS_THEN_CLIENT -qmgrHostname 10.87.205.69 -qmgrPortNumber 5433 -qmgrSvrconnChannel SYSTEM.DEF.SRVCONN '
asAttrs += '-stopEndpointIfDeliveryFails false -customProperties [[useJNDI true][maxPoolDepth 3]] -destinationType javax.jms.Queue'
isExist = 1
for asId in activationSpecs:
	if AdminConfig.showAttribute( asId, 'jndiName' ) == activationSpecName:
		print '[Waring] : Activation Specification (%s) %salready Exist%s'%(activationSpecName,YELLOW,END)
		if isSkipIfExist == 1:
			echoMessage = '[Warning] : %sDeleting%s Activation Specification (%s)'% (RED,END,activationSpecName)
			print echoMessage,
			AdminTask.deleteWMQActivationSpec(asId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Activation Specification (%s)'% (YELLOW,END,activationSpecName)
			isExist = 0
		break
if isExist == 1:
	echoMessage = '[Info] : Creating Activation Specification (%s)'% activationSpecName
	print echoMessage,
	done = AdminTask.createWMQActivationSpec( scopeID, asAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()

# ----------------------- Activation Spec  EAItoWPSFetchOffersReceiveQueueAS_SCRM------------------------------------------------------
activationSpecName = 'jms/EAItoWPSFetchOffersReceiveQueueAS_SCRM'
asAttrs = '-name EAItoWPSFetchOffersReceiveQueueAS_SCRM -jndiName jms/EAItoWPSFetchOffersReceiveQueueAS_SCRM -destinationJndiName jms/EAItoWPSFetchOffersReceiveQueue_SCRM -qmgrName QMEIBAU1 '
asAttrs += '-wmqTransportType BINDINGS_THEN_CLIENT -qmgrHostname 10.87.205.69 -qmgrPortNumber 5433 -qmgrSvrconnChannel SYSTEM.DEF.SRVCONN '
asAttrs += '-stopEndpointIfDeliveryFails false -customProperties [[useJNDI true][maxPoolDepth 3]] -destinationType javax.jms.Queue'
isExist = 1
for asId in activationSpecs:
	if AdminConfig.showAttribute( asId, 'jndiName' ) == activationSpecName:
		print '[Waring] : Activation Specification (%s) %salready Exist%s'%(activationSpecName,YELLOW,END)
		if isSkipIfExist == 1:
			echoMessage = '[Warning] : %sDeleting%s Activation Specification (%s)'% (RED,END,activationSpecName)
			print echoMessage,
			AdminTask.deleteWMQActivationSpec(asId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Activation Specification (%s)'% (YELLOW,END,activationSpecName)
			isExist = 0
		break
if isExist == 1:
	echoMessage = '[Info] : Creating Activation Specification (%s)'% activationSpecName
	print echoMessage,
	done = AdminTask.createWMQActivationSpec( scopeID, asAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()

# ----------------------- Activation Spec  CRM_REDCUSTOMER_AS_SCRM------------------------------------------------------
activationSpecName = 'jms/CRM_REDCUSTOMER_AS_SCRM'
asAttrs = '-name CRM_REDCUSTOMER_AS_SCRM -jndiName jms/CRM_REDCUSTOMER_AS_SCRM -destinationJndiName jms/CRM_REDCUSTOMER_RQO_SCRM -qmgrName QMEIBAU1 '
asAttrs += '-wmqTransportType BINDINGS_THEN_CLIENT -qmgrHostname 10.87.205.69 -qmgrPortNumber 5433 -qmgrSvrconnChannel SYSTEM.DEF.SRVCONN '
asAttrs += '-stopEndpointIfDeliveryFails false -customProperties [[useJNDI true][maxPoolDepth 3]] -destinationType javax.jms.Queue'
isExist = 1
for asId in activationSpecs:
	if AdminConfig.showAttribute( asId, 'jndiName' ) == activationSpecName:
		print '[Waring] : Activation Specification (%s) %salready Exist%s'%(activationSpecName,YELLOW,END)
		if isSkipIfExist == 1:
			echoMessage = '[Warning] : %sDeleting%s Activation Specification (%s)'% (RED,END,activationSpecName)
			print echoMessage,
			AdminTask.deleteWMQActivationSpec(asId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Activation Specification (%s)'% (YELLOW,END,activationSpecName)
			isExist = 0
		break
if isExist == 1:
	echoMessage = '[Info] : Creating Activation Specification (%s)'% activationSpecName
	print echoMessage,
	done = AdminTask.createWMQActivationSpec( scopeID, asAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()

# ----------------------- QCF Creation DOX_REDCUSTOMER_OutMQCF_SCRM------------------------------------------------------
qcfname = 'jms/DOX_REDCUSTOMER_OutMQCF_SCRM'
qcfAttrs = '-type QCF -name DOX_REDCUSTOMER_OutMQCF_SCRM -jndiName jms/DOX_REDCUSTOMER_OutMQCF_SCRM -qmgrName QMEIIU1 -wmqTransportType BINDINGS_THEN_CLIENT '
qcfAttrs += '-qmgrHostname 10.87.205.67 -qmgrPortNumber 5233 -qmgrSvrconnChannel SYSTEM.DEF.SVRCONN'
isExist = 1
deleteQcfId =''
for qcfId in connectionFactories:
	if AdminConfig.showAttribute( qcfId, 'jndiName' ) == qcfname:
		print '[Waring] : Queue Connetion Factory (%s) %salready Exist%s'%(qcfname,YELLOW,END)
		if isSkipIfExist == 1:
			echoMessage = '[Warning] : %sDeleting%s Queue Connetion Factory'% (RED,END,qcfname)
			print echoMessage,
			AdminTask.deleteWMQConnectionFactory(qcfId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Connetion Factory  (%s)'% (YELLOW,END,qcfname)
			isExist = 0
		break
if isExist == 1:
	echoMessage = '[Info] : Creating Queue Connetion Factory (%s)'% qcfname
	print echoMessage,
	done = AdminTask.createWMQConnectionFactory( scopeID, qcfAttrs )
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- QCF Creation DOX_Common_CF_SCRM------------------------------------------------------
qcfname = 'jms/DOX_Common_CF_SCRM'
qcfAttrs = '-type QCF -name DOX_Common_CF_SCRM -jndiName jms/DOX_Common_CF_SCRM -qmgrName QMEIIU1 -wmqTransportType BINDINGS_THEN_CLIENT '
qcfAttrs += '-qmgrHostname 10.87.205.67 -qmgrPortNumber 5233 -qmgrSvrconnChannel SYSTEM.DEF.SVRCONN'
isExist = 1
deleteQcfId =''
for qcfId in connectionFactories:
	if AdminConfig.showAttribute( qcfId, 'jndiName' ) == qcfname:
		print '[Waring] : Queue Connetion Factory (%s) %salready Exist%s'%(qcfname,YELLOW,END)
		if isSkipIfExist == 1:
			echoMessage = '[Warning] : %sDeleting%s Queue Connetion Factory'% (RED,END,qcfname)
			print echoMessage,
			AdminTask.deleteWMQConnectionFactory(qcfId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Connetion Factory  (%s)'% (YELLOW,END,qcfname)
			isExist = 0
		break
if isExist == 1:
	echoMessage = '[Info] : Creating Queue Connetion Factory (%s)'% qcfname
	print echoMessage,
	done = AdminTask.createWMQConnectionFactory( scopeID, qcfAttrs )
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- QCF Creation AUDIT_FMNP2_OutMQCF_SCRM------------------------------------------------------
qcfname = 'jms/AUDIT_FMNP2_OutMQCF_SCRM'
qcfAttrs = '-type QCF -name AUDIT_FMNP2_OutMQCF_SCRM -jndiName jms/AUDIT_FMNP2_OutMQCF_SCRM -qmgrName QMEIIU1 -wmqTransportType BINDINGS_THEN_CLIENT '
qcfAttrs += '-qmgrHostname 10.87.205.67 -qmgrPortNumber 5233 -qmgrSvrconnChannel SYSTEM.DEF.SVRCONN'
isExist = 1
deleteQcfId =''
for qcfId in connectionFactories:
	if AdminConfig.showAttribute( qcfId, 'jndiName' ) == qcfname:
		print '[Waring] : Queue Connetion Factory (%s) %salready Exist%s'%(qcfname,YELLOW,END)
		if isSkipIfExist == 1:
			echoMessage = '[Warning] : %sDeleting%s Queue Connetion Factory'% (RED,END,qcfname)
			print echoMessage,
			AdminTask.deleteWMQConnectionFactory(qcfId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Connetion Factory  (%s)'% (YELLOW,END,qcfname)
			isExist = 0
		break
if isExist == 1:
	echoMessage = '[Info] : Creating Queue Connetion Factory (%s)'% qcfname
	print echoMessage,
	done = AdminTask.createWMQConnectionFactory( scopeID, qcfAttrs )
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- QCF Creation RED_Delink_RECC_CommonCF_SCRM------------------------------------------------------
qcfname = 'jms/RED_Delink_RECC_CommonCF_SCRM'
qcfAttrs = '-type QCF -name RED_Delink_RECC_CommonCF_SCRM -jndiName jms/RED_Delink_RECC_CommonCF_SCRM -qmgrName QMEIIU1 -wmqTransportType BINDINGS_THEN_CLIENT '
qcfAttrs += '-qmgrHostname 10.87.205.67 -qmgrPortNumber 5233 -qmgrSvrconnChannel SYSTEM.DEF.SVRCONN'
isExist = 1
deleteQcfId =''
for qcfId in connectionFactories:
	if AdminConfig.showAttribute( qcfId, 'jndiName' ) == qcfname:
		print '[Waring] : Queue Connetion Factory (%s) %salready Exist%s'%(qcfname,YELLOW,END)
		if isSkipIfExist == 1:
			echoMessage = '[Warning] : %sDeleting%s Queue Connetion Factory'% (RED,END,qcfname)
			print echoMessage,
			AdminTask.deleteWMQConnectionFactory(qcfId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Connetion Factory  (%s)'% (YELLOW,END,qcfname)
			isExist = 0
		break
if isExist == 1:
	echoMessage = '[Info] : Creating Queue Connetion Factory (%s)'% qcfname
	print echoMessage,
	done = AdminTask.createWMQConnectionFactory( scopeID, qcfAttrs )
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- QCF Creation CRM_REDCUSTOMER_EAI_OUTRPI_SCRM------------------------------------------------------
qcfname = 'jms/CRM_REDCUSTOMER_EAI_OUTRPI_SCRM'
qcfAttrs = '-type QCF -name CRM_REDCUSTOMER_EAI_OUTRPI_SCRM -jndiName jms/CRM_REDCUSTOMER_EAI_OUTRPI_SCRM -qmgrName QMEIIU1 -wmqTransportType BINDINGS_THEN_CLIENT '
qcfAttrs += '-qmgrHostname 10.87.205.67 -qmgrPortNumber 5233 -qmgrSvrconnChannel SYSTEM.DEF.SVRCONN'
isExist = 1
deleteQcfId =''
for qcfId in connectionFactories:
	if AdminConfig.showAttribute( qcfId, 'jndiName' ) == qcfname:
		print '[Waring] : Queue Connetion Factory (%s) %salready Exist%s'%(qcfname,YELLOW,END)
		if isSkipIfExist == 1:
			echoMessage = '[Warning] : %sDeleting%s Queue Connetion Factory'% (RED,END,qcfname)
			print echoMessage,
			AdminTask.deleteWMQConnectionFactory(qcfId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Connetion Factory  (%s)'% (YELLOW,END,qcfname)
			isExist = 0
		break
if isExist == 1:
	echoMessage = '[Info] : Creating Queue Connetion Factory (%s)'% qcfname
	print echoMessage,
	done = AdminTask.createWMQConnectionFactory( scopeID, qcfAttrs )
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- Queue JNDI Creation DOX_CHNGPRICEPLAN_WRITE_RQI_SCRM------------------------------------------------------
queueName = 'jms/DOX_CHNGPRICEPLAN_WRITE_RQI_SCRM'
mqqAttrs = '-name DOX_CHNGPRICEPLAN_WRITE_RQI_SCRM -jndiName jms/DOX_CHNGPRICEPLAN_WRITE_RQI_SCRM -queueName DOX.SUBSBRSRV.ESB.RQI.EXT.02 '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
isExist = 1
for qId in queues:
	if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
		print '[Warning] :  Queue Jndi (%s) %salready Exist%s'%(queueName,YELLOW,END)
		if isSkipIfExist == 1 :
			echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
			print echoMessage,
			AdminTask.deleteWMQQueue(qId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
			isExist = 0
		break
if isExist == 1:	
	echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
	print echoMessage,
	done = AdminTask.createWMQQueue( scopeID, mqqAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- Queue JNDI Creation DOX_CHNGBIILINGARRANGEMENT_WRITE_RQI_SCRM------------------------------------------------------
queueName = 'jms/DOX_CHNGBIILINGARRANGEMENT_WRITE_RQI_SCRM'
mqqAttrs = '-name DOX_CHNGBIILINGARRANGEMENT_WRITE_RQI_SCRM -jndiName jms/DOX_CHNGBIILINGARRANGEMENT_WRITE_RQI_SCRM -queueName DOX.BLARGMT.ESB.RQI.02 '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
isExist = 1
for qId in queues:
	if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
		print '[Warning] :  Queue Jndi (%s) %salready Exist%s'%(queueName,YELLOW,END)
		if isSkipIfExist == 1 :
			echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
			print echoMessage,
			AdminTask.deleteWMQQueue(qId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
			isExist = 0
		break
if isExist == 1:	
	echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
	print echoMessage,
	done = AdminTask.createWMQQueue( scopeID, mqqAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- Queue JNDI Creation DOX_MVSUBSCRIBER_WRITE_RQI_SCRM------------------------------------------------------
queueName = 'jms/DOX_MVSUBSCRIBER_WRITE_RQI_SCRM'
mqqAttrs = '-name DOX_MVSUBSCRIBER_WRITE_RQI_SCRM -jndiName jms/DOX_MVSUBSCRIBER_WRITE_RQI_SCRM -queueName DOX.SUBSBRSRV.ESB.RQI.02 '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
isExist = 1
for qId in queues:
	if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
		print '[Warning] :  Queue Jndi (%s) %salready Exist%s'%(queueName,YELLOW,END)
		if isSkipIfExist == 1 :
			echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
			print echoMessage,
			AdminTask.deleteWMQQueue(qId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
			isExist = 0
		break
if isExist == 1:	
	echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
	print echoMessage,
	done = AdminTask.createWMQQueue( scopeID, mqqAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- Queue JNDI Creation FMNP2_GET_ENTITY_DONAR_RQI_SCRM------------------------------------------------------
queueName = 'jms/FMNP2_GET_ENTITY_DONAR_RQI_SCRM'
mqqAttrs = '-name FMNP2_GET_ENTITY_DONAR_RQI_SCRM -jndiName jms/FMNP2_GET_ENTITY_DONAR_RQI_SCRM -queueName DOX.SEARCHSRV.ESB.RQI.01 '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
isExist = 1
for qId in queues:
	if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
		print '[Warning] :  Queue Jndi (%s) %salready Exist%s'%(queueName,YELLOW,END)
		if isSkipIfExist == 1 :
			echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
			print echoMessage,
			AdminTask.deleteWMQQueue(qId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
			isExist = 0
		break
if isExist == 1:	
	echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
	print echoMessage,
	done = AdminTask.createWMQQueue( scopeID, mqqAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- Queue JNDI Creation DOX_GETAGREEMENTINFO_READ_RQI_SCRM------------------------------------------------------
queueName = 'jms/DOX_GETAGREEMENTINFO_READ_RQI_SCRM'
mqqAttrs = '-name DOX_GETAGREEMENTINFO_READ_RQI_SCRM -jndiName jms/DOX_GETAGREEMENTINFO_READ_RQI_SCRM -queueName DOX.AGRMNT.ESB.RQI.01 '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
isExist = 1
for qId in queues:
	if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
		print '[Warning] :  Queue Jndi (%s) %salready Exist%s'%(queueName,YELLOW,END)
		if isSkipIfExist == 1 :
			echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
			print echoMessage,
			AdminTask.deleteWMQQueue(qId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
			isExist = 0
		break
if isExist == 1:	
	echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
	print echoMessage,
	done = AdminTask.createWMQQueue( scopeID, mqqAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- Queue JNDI Creation DOX_GETBILLINGARRANGEMENT_READ_RQI_SCRM------------------------------------------------------
queueName = 'jms/DOX_GETBILLINGARRANGEMENT_READ_RQI_SCRM'
mqqAttrs = '-name DOX_GETBILLINGARRANGEMENT_READ_RQI_SCRM -jndiName jms/DOX_GETBILLINGARRANGEMENT_READ_RQI_SCRM -queueName DOX.BLARGMT.ESB.RQI.01 '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
isExist = 1
for qId in queues:
	if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
		print '[Warning] :  Queue Jndi (%s) %salready Exist%s'%(queueName,YELLOW,END)
		if isSkipIfExist == 1 :
			echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
			print echoMessage,
			AdminTask.deleteWMQQueue(qId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
			isExist = 0
		break
if isExist == 1:	
	echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
	print echoMessage,
	done = AdminTask.createWMQQueue( scopeID, mqqAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- Queue JNDI Creation DOX_PARENTINFO_READ_RQI_SCRM------------------------------------------------------
queueName = 'jms/DOX_PARENTINFO_READ_RQI_SCRM'
mqqAttrs = '-name DOX_PARENTINFO_READ_RQI_SCRM -jndiName jms/DOX_PARENTINFO_READ_RQI_SCRM -queueName DOX.CUSTHRCHY.ESB.RQI.01 '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
isExist = 1
for qId in queues:
	if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
		print '[Warning] :  Queue Jndi (%s) %salready Exist%s'%(queueName,YELLOW,END)
		if isSkipIfExist == 1 :
			echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
			print echoMessage,
			AdminTask.deleteWMQQueue(qId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
			isExist = 0
		break
if isExist == 1:	
	echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
	print echoMessage,
	done = AdminTask.createWMQQueue( scopeID, mqqAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- Queue JNDI Creation DOX_UPDATEAGREEMENT_RAED_RQI_SCRM------------------------------------------------------
queueName = 'jms/DOX_UPDATEAGREEMENT_RAED_RQI_SCRM'
mqqAttrs = '-name DOX_UPDATEAGREEMENT_RAED_RQI_SCRM -jndiName jms/DOX_UPDATEAGREEMENT_RAED_RQI_SCRM -queueName DOX.AGRMNT.ESB.RQI.02 '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
isExist = 1
for qId in queues:
	if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
		print '[Warning] :  Queue Jndi (%s) %salready Exist%s'%(queueName,YELLOW,END)
		if isSkipIfExist == 1 :
			echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
			print echoMessage,
			AdminTask.deleteWMQQueue(qId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
			isExist = 0
		break
if isExist == 1:	
	echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
	print echoMessage,
	done = AdminTask.createWMQQueue( scopeID, mqqAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- Queue JNDI Creation DOX_AUDIT_OutRQO_AP1_SCRM------------------------------------------------------
queueName = 'jms/DOX_AUDIT_OutRQO_AP1_SCRM'
mqqAttrs = '-name DOX_AUDIT_OutRQO_AP1_SCRM -jndiName jms/DOX_AUDIT_OutRQO_AP1_SCRM -queueName DOX.ESB.AUI.02 '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
isExist = 1
for qId in queues:
	if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
		print '[Warning] :  Queue Jndi (%s) %salready Exist%s'%(queueName,YELLOW,END)
		if isSkipIfExist == 1 :
			echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
			print echoMessage,
			AdminTask.deleteWMQQueue(qId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
			isExist = 0
		break
if isExist == 1:	
	echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
	print echoMessage,
	done = AdminTask.createWMQQueue( scopeID, mqqAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- Queue JNDI Creation BPMToEAIRECCSubPkgSendQ_SCRM------------------------------------------------------
queueName = 'jms/BPMToEAIRECCSubPkgSendQ_SCRM'
mqqAttrs = '-name BPMToEAIRECCSubPkgSendQ_SCRM -jndiName jms/BPMToEAIRECCSubPkgSendQ_SCRM -queueName APPS.RECC.CHGSUBSBR.ESB.RQI.EXT.02 '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
isExist = 1
for qId in queues:
	if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
		print '[Warning] :  Queue Jndi (%s) %salready Exist%s'%(queueName,YELLOW,END)
		if isSkipIfExist == 1 :
			echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
			print echoMessage,
			AdminTask.deleteWMQQueue(qId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
			isExist = 0
		break
if isExist == 1:	
	echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
	print echoMessage,
	done = AdminTask.createWMQQueue( scopeID, mqqAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- Queue JNDI Creation WPSToEAIRECCDELSendQueue_SCRM------------------------------------------------------
queueName = 'jms/WPSToEAIRECCDELSendQueue_SCRM'
mqqAttrs = '-name WPSToEAIRECCDELSendQueue_SCRM -jndiName jms/WPSToEAIRECCDELSendQueue_SCRM -queueName APPS.RECC.DELSUBSBR.ESB.PE.RQI.02 '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
isExist = 1
for qId in queues:
	if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
		print '[Warning] :  Queue Jndi (%s) %salready Exist%s'%(queueName,YELLOW,END)
		if isSkipIfExist == 1 :
			echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
			print echoMessage,
			AdminTask.deleteWMQQueue(qId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
			isExist = 0
		break
if isExist == 1:	
	echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
	print echoMessage,
	done = AdminTask.createWMQQueue( scopeID, mqqAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- Queue JNDI Creation AdapterToEAIRECCSendQueue_SCRM------------------------------------------------------
queueName = 'jms/AdapterToEAIRECCSendQueue_SCRM'
mqqAttrs = '-name AdapterToEAIRECCSendQueue_SCRM -jndiName jms/AdapterToEAIRECCSendQueue_SCRM -queueName APPS.REDCUSTOMER.ESB.UPG.RQI.01 '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
isExist = 1
for qId in queues:
	if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
		print '[Warning] :  Queue Jndi (%s) %salready Exist%s'%(queueName,YELLOW,END)
		if isSkipIfExist == 1 :
			echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
			print echoMessage,
			AdminTask.deleteWMQQueue(qId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
			isExist = 0
		break
if isExist == 1:	
	echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
	print echoMessage,
	done = AdminTask.createWMQQueue( scopeID, mqqAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- Queue JNDI Creation WPSToEAIFetchOffersSendQueue_SCRM------------------------------------------------------
queueName = 'jms/WPSToEAIFetchOffersSendQueue_SCRM'
mqqAttrs = '-name WPSToEAIFetchOffersSendQueue_SCRM -jndiName jms/WPSToEAIFetchOffersSendQueue_SCRM -queueName APPS.RECC.RBTUPSRV.ESB.RQI.01 '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
isExist = 1
for qId in queues:
	if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
		print '[Warning] :  Queue Jndi (%s) %salready Exist%s'%(queueName,YELLOW,END)
		if isSkipIfExist == 1 :
			echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
			print echoMessage,
			AdminTask.deleteWMQQueue(qId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
			isExist = 0
		break
if isExist == 1:	
	echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
	print echoMessage,
	done = AdminTask.createWMQQueue( scopeID, mqqAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- Queue JNDI Creation CRM_REDCUSTOMER_RPI_SCRM------------------------------------------------------
queueName = 'jms/CRM_REDCUSTOMER_RPI_SCRM'
mqqAttrs = '-name CRM_REDCUSTOMER_RPI_SCRM -jndiName jms/CRM_REDCUSTOMER_RPI_SCRM -queueName APPS.SCRM.ESB.REDCUSTCRT.RPI.02 '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
isExist = 1
for qId in queues:
	if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
		print '[Warning] :  Queue Jndi (%s) %salready Exist%s'%(queueName,YELLOW,END)
		if isSkipIfExist == 1 :
			echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
			print echoMessage,
			AdminTask.deleteWMQQueue(qId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
			isExist = 0
		break
if isExist == 1:	
	echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
	print echoMessage,
	done = AdminTask.createWMQQueue( scopeID, mqqAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- Queue JNDI Creation DOX_CHNGPRICEPLAN_WRITE_RPO_SCRM------------------------------------------------------
queueName = 'jms/DOX_CHNGPRICEPLAN_WRITE_RPO_SCRM'
mqqAttrs = '-name DOX_CHNGPRICEPLAN_WRITE_RPO_SCRM -jndiName jms/DOX_CHNGPRICEPLAN_WRITE_RPO_SCRM -queueName DOX.SCRM.CHNGPRICEPLAN.WRITE.UPG.RPO.02 '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
isExist = 1
for qId in queues:
	if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
		print '[Warning] :  Queue Jndi (%s) %salready Exist%s'%(queueName,YELLOW,END)
		if isSkipIfExist == 1 :
			echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
			print echoMessage,
			AdminTask.deleteWMQQueue(qId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
			isExist = 0
		break
if isExist == 1:	
	echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
	print echoMessage,
	done = AdminTask.createWMQQueue( scopeID, mqqAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- Queue JNDI Creation DOX_CHNGBIILINGARRANGEMENT_WRITE_RPO_SCRM------------------------------------------------------
queueName = 'jms/DOX_CHNGBIILINGARRANGEMENT_WRITE_RPO_SCRM'
mqqAttrs = '-name DOX_CHNGBIILINGARRANGEMENT_WRITE_RPO_SCRM -jndiName jms/DOX_CHNGBIILINGARRANGEMENT_WRITE_RPO_SCRM -queueName DOX.SCRM.CHNGBIILINGARRANGEMENT.WRITE.UPG.RPO.02 '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
isExist = 1
for qId in queues:
	if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
		print '[Warning] :  Queue Jndi (%s) %salready Exist%s'%(queueName,YELLOW,END)
		if isSkipIfExist == 1 :
			echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
			print echoMessage,
			AdminTask.deleteWMQQueue(qId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
			isExist = 0
		break
if isExist == 1:	
	echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
	print echoMessage,
	done = AdminTask.createWMQQueue( scopeID, mqqAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- Queue JNDI Creation DOX_MVSUBSCRIBER_WRITE_RPO_SCRM------------------------------------------------------
queueName = 'jms/DOX_MVSUBSCRIBER_WRITE_RPO_SCRM'
mqqAttrs = '-name DOX_MVSUBSCRIBER_WRITE_RPO_SCRM -jndiName jms/DOX_MVSUBSCRIBER_WRITE_RPO_SCRM -queueName DOX.SCRM.MVSUBSCRIBER.WRITE.UPG.RPO.02 '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
isExist = 1
for qId in queues:
	if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
		print '[Warning] :  Queue Jndi (%s) %salready Exist%s'%(queueName,YELLOW,END)
		if isSkipIfExist == 1 :
			echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
			print echoMessage,
			AdminTask.deleteWMQQueue(qId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
			isExist = 0
		break
if isExist == 1:	
	echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
	print echoMessage,
	done = AdminTask.createWMQQueue( scopeID, mqqAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- Queue JNDI Creation DOX_SEARCHENTITY_READ_RPO_SCRM------------------------------------------------------
queueName = 'jms/DOX_SEARCHENTITY_READ_RPO_SCRM'
mqqAttrs = '-name DOX_SEARCHENTITY_READ_RPO_SCRM -jndiName jms/DOX_SEARCHENTITY_READ_RPO_SCRM -queueName DOX.SCRM.SEARCHENTITY.READ.UPG.RPO.02 '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
isExist = 1
for qId in queues:
	if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
		print '[Warning] :  Queue Jndi (%s) %salready Exist%s'%(queueName,YELLOW,END)
		if isSkipIfExist == 1 :
			echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
			print echoMessage,
			AdminTask.deleteWMQQueue(qId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
			isExist = 0
		break
if isExist == 1:	
	echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
	print echoMessage,
	done = AdminTask.createWMQQueue( scopeID, mqqAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- Queue JNDI Creation DOX_GETAGREEMENTINFO_READ_RPO_SCRM------------------------------------------------------
queueName = 'jms/DOX_GETAGREEMENTINFO_READ_RPO_SCRM'
mqqAttrs = '-name DOX_GETAGREEMENTINFO_READ_RPO_SCRM -jndiName jms/DOX_GETAGREEMENTINFO_READ_RPO_SCRM -queueName DOX.SCRM.GETAGREEMENTINFO.READ.UPG.RPO.02 '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
isExist = 1
for qId in queues:
	if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
		print '[Warning] :  Queue Jndi (%s) %salready Exist%s'%(queueName,YELLOW,END)
		if isSkipIfExist == 1 :
			echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
			print echoMessage,
			AdminTask.deleteWMQQueue(qId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
			isExist = 0
		break
if isExist == 1:	
	echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
	print echoMessage,
	done = AdminTask.createWMQQueue( scopeID, mqqAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- Queue JNDI Creation DOX_GETBILLINGARRANGEMENT_READ_RPO_SCRM------------------------------------------------------
queueName = 'jms/DOX_GETBILLINGARRANGEMENT_READ_RPO_SCRM'
mqqAttrs = '-name DOX_GETBILLINGARRANGEMENT_READ_RPO_SCRM -jndiName jms/DOX_GETBILLINGARRANGEMENT_READ_RPO_SCRM -queueName DOX.SCRM.GETBILLINGARRANGEMENT.UPG.READ.RPO '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
isExist = 1
for qId in queues:
	if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
		print '[Warning] :  Queue Jndi (%s) %salready Exist%s'%(queueName,YELLOW,END)
		if isSkipIfExist == 1 :
			echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
			print echoMessage,
			AdminTask.deleteWMQQueue(qId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
			isExist = 0
		break
if isExist == 1:	
	echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
	print echoMessage,
	done = AdminTask.createWMQQueue( scopeID, mqqAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- Queue JNDI Creation DOX_PARENTINFO_READ_RPO_SCRM------------------------------------------------------
queueName = 'jms/DOX_PARENTINFO_READ_RPO_SCRM'
mqqAttrs = '-name DOX_PARENTINFO_READ_RPO_SCRM -jndiName jms/DOX_PARENTINFO_READ_RPO_SCRM -queueName DOX.SCRM.PARENTINFO.READ.UPG.RPO.02 '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
isExist = 1
for qId in queues:
	if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
		print '[Warning] :  Queue Jndi (%s) %salready Exist%s'%(queueName,YELLOW,END)
		if isSkipIfExist == 1 :
			echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
			print echoMessage,
			AdminTask.deleteWMQQueue(qId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
			isExist = 0
		break
if isExist == 1:	
	echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
	print echoMessage,
	done = AdminTask.createWMQQueue( scopeID, mqqAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- Queue JNDI Creation DOX_UPDATEAGREEMENT_READ_RPO_SCRM------------------------------------------------------
queueName = 'jms/DOX_UPDATEAGREEMENT_READ_RPO_SCRM'
mqqAttrs = '-name DOX_UPDATEAGREEMENT_READ_RPO_SCRM -jndiName jms/DOX_UPDATEAGREEMENT_READ_RPO_SCRM -queueName DOX.SCRM.UPDATEAGREEMENT.READ.UPG.RPO.02 '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
isExist = 1
for qId in queues:
	if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
		print '[Warning] :  Queue Jndi (%s) %salready Exist%s'%(queueName,YELLOW,END)
		if isSkipIfExist == 1 :
			echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
			print echoMessage,
			AdminTask.deleteWMQQueue(qId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
			isExist = 0
		break
if isExist == 1:	
	echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
	print echoMessage,
	done = AdminTask.createWMQQueue( scopeID, mqqAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- Queue JNDI Creation EAIToBPMREDPESubOfferReceiveQ_SCRM------------------------------------------------------
queueName = 'jms/EAIToBPMREDPESubOfferReceiveQ_SCRM'
mqqAttrs = '-name EAIToBPMREDPESubOfferReceiveQ_SCRM -jndiName jms/EAIToBPMREDPESubOfferReceiveQ_SCRM -queueName APPS.SCRM.REDPLUS.PE.CHGSUBSBR.ESB.RPO.02 '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
isExist = 1
for qId in queues:
	if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
		print '[Warning] :  Queue Jndi (%s) %salready Exist%s'%(queueName,YELLOW,END)
		if isSkipIfExist == 1 :
			echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
			print echoMessage,
			AdminTask.deleteWMQQueue(qId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
			isExist = 0
		break
if isExist == 1:	
	echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
	print echoMessage,
	done = AdminTask.createWMQQueue( scopeID, mqqAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- Queue JNDI Creation EAItoWPSRECCDELReceiveQueue_SCRM------------------------------------------------------
queueName = 'jms/EAItoWPSRECCDELReceiveQueue_SCRM'
mqqAttrs = '-name EAItoWPSRECCDELReceiveQueue_SCRM -jndiName jms/EAItoWPSRECCDELReceiveQueue_SCRM -queueName APPS.SCRM.DELSUBSBR.BPM.REDPLUS.RPO.01 '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
isExist = 1
for qId in queues:
	if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
		print '[Warning] :  Queue Jndi (%s) %salready Exist%s'%(queueName,YELLOW,END)
		if isSkipIfExist == 1 :
			echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
			print echoMessage,
			AdminTask.deleteWMQQueue(qId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
			isExist = 0
		break
if isExist == 1:	
	echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
	print echoMessage,
	done = AdminTask.createWMQQueue( scopeID, mqqAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- Queue JNDI Creation EAItoAdapterRECCReceiveQueue_SCRM------------------------------------------------------
queueName = 'jms/EAItoAdapterRECCReceiveQueue_SCRM'
mqqAttrs = '-name EAItoAdapterRECCReceiveQueue_SCRM -jndiName jms/EAItoAdapterRECCReceiveQueue_SCRM -queueName APPS.SCRM.REDPLUSCUSTOMER.ESB.RPO.01 '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
isExist = 1
for qId in queues:
	if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
		print '[Warning] :  Queue Jndi (%s) %salready Exist%s'%(queueName,YELLOW,END)
		if isSkipIfExist == 1 :
			echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
			print echoMessage,
			AdminTask.deleteWMQQueue(qId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
			isExist = 0
		break
if isExist == 1:	
	echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
	print echoMessage,
	done = AdminTask.createWMQQueue( scopeID, mqqAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- Queue JNDI Creation EAItoWPSFetchOffersReceiveQueue_SCRM------------------------------------------------------
queueName = 'jms/EAItoWPSFetchOffersReceiveQueue_SCRM'
mqqAttrs = '-name EAItoWPSFetchOffersReceiveQueue_SCRM -jndiName jms/EAItoWPSFetchOffersReceiveQueue_SCRM -queueName APPS.SCRM.RECC.RBTUPSRV.WPS.UPG.RPO.02 '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
isExist = 1
for qId in queues:
	if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
		print '[Warning] :  Queue Jndi (%s) %salready Exist%s'%(queueName,YELLOW,END)
		if isSkipIfExist == 1 :
			echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
			print echoMessage,
			AdminTask.deleteWMQQueue(qId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
			isExist = 0
		break
if isExist == 1:	
	echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
	print echoMessage,
	done = AdminTask.createWMQQueue( scopeID, mqqAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
# ----------------------- Queue JNDI Creation CRM_REDCUSTOMER_RQO_SCRM------------------------------------------------------
queueName = 'jms/CRM_REDCUSTOMER_RQO_SCRM'
mqqAttrs = '-name CRM_REDCUSTOMER_RQO_SCRM -jndiName jms/CRM_REDCUSTOMER_RQO_SCRM -queueName APPS.SCRM.ESB.REDCUSTCRT.RQO.02 '
mqqAttrs += '-customProperties [[MDREAD YES] [MSGBODY MQ] [MDWRITE YES]]'
isExist = 1
for qId in queues:
	if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
		print '[Warning] :  Queue Jndi (%s) %salready Exist%s'%(queueName,YELLOW,END)
		if isSkipIfExist == 1 :
			echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
			print echoMessage,
			AdminTask.deleteWMQQueue(qId)
			print '.' * (100 - len(echoMessage)),
			print '[ %sDONE%s ]'%(GREEN,END)
			isExist = 1
			AdminConfig.save()
		else:
			print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
			isExist = 0
		break
if isExist == 1:	
	echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
	print echoMessage,
	done = AdminTask.createWMQQueue( scopeID, mqqAttrs ) 
	print '.' * (100 - len(echoMessage)),
	if done:
		print '[ %sDONE%s ]'%(GREEN,END)
	else:
		print '[ %sERROR%s ]'%(RED,END)
AdminConfig.save()
echoMessage="Saving to master repository"
print echoMessage,
AdminConfig.save() 
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'

echoMessage="Synchronizing nodes"
print echoMessage,
#SyncNodes()
print '.' * (100 - len(echoMessage)),
print '[ DONE ]'
print '\n *** End of script ***'

   	
#------------------------------------------------------------------------------
# Queue Creation
#------------------------------------------------------------------------------
def createQueueJndi(asAttrs,queueName):
	isExist = 1
	global isSkipIfExist
	global queues
	global YELLOW
	global RED
	global GREEN
	global END
	for qId in queues:
		if AdminConfig.showAttribute( qId, 'jndiName' ) == queueName:
			print '%s[Waring] :  Queue Jndi (%s) already Exist%s'%(YELLOW,queueName,END)
			if isSkipIfExist == 1:
				echoMessage = '[Warning] : %sDeleting%s Queue Jndi (%s)'% (RED,END,queueName)
				print echoMessage,
				done = AdminTask.deleteWMQQueue(qId)
				print '.' * (100 - len(echoMessage)),
				if done:
					print '[ %sDONE%s ]'%(GREEN,END)
					isExist = 1
				else:
					print '[ %sERROR%s ]'%(RED,END)
					isExist = 0
			else:
				print '[Warning] : %sSkipping%s Queue Jndi (%s)'% (YELLOW,END,queueName)
				isExist = 0
				
	if isExist == 1:	
		echoMessage = '[Info] : Creating Queue Jndi (%s)'% queueName
		print echoMessage
		done = AdminTask.createWMQQueue( scopeID, asAttrs ) 
		print '.' * (100 - len(echoMessage)),
		if done:
			print '[ %sDONE%s ]'%(GREEN,END)
		else:
			print '[ %sERROR%s ]'%(RED,END)

#------------------------------------------------------------------------------
# Activation Spec Creation
#------------------------------------------------------------------------------
def createActivationSpec(asAttrs,activationSpecName):
	isExist = 1
	global isSkipIfExist
	global activationSpecs
	global YELLOW
	global RED
	global GREEN
	global END
	for asId in activationSpecs:
		if AdminConfig.showAttribute( asId, 'jndiName' ) == activationSpecName:
			print '%s[Waring] : Activation Specification (%s) already Exist%s'%(YELLOW,activationSpecName,END)
			if isSkipIfExist == 1:
				echoMessage = '[Warning] : %sDeleting%s Activation Specification (%s)'% (RED,END,activationSpecName)
				print echoMessage,
				done = AdminTask.deleteWMQActivationSpec(asId)
				print '.' * (100 - len(echoMessage)),
				if done:
					print '[ %sDONE%s ]'%(GREEN,END)
					isExist = 1
				else:
					print '[ %sERROR%s ]'%(RED,END)
					isExist = 0
			else:
				print '[Warning] : %sSkipping%s Activation Specification (%s)'% (YELLOW,END,activationSpecName)
				isExist = 0
				
	if isExist == 1:
		echoMessage = '[Info] : Creating Activation Specification (%s)'% activationSpecName
		print echoMessage,
		done = AdminTask.createWMQActivationSpec( scopeID, asAttrs ) 
		print '.' * (100 - len(echoMessage)),
		if done:
			print '[ %sDONE%s ]'%(GREEN,END)
		else:
			print '[ %sERROR%s ]'%(RED,END)

#------------------------------------------------------------------------------
# Queue Connection Factory Creation
#------------------------------------------------------------------------------
def createQueueConnetionFactory(asAttrs,qcfname):
	isExist = 1
	global isSkipIfExist
	global connectionFactories
	global YELLOW
	global RED
	global GREEN
	global END
	for qcfId in connectionFactories:
		if AdminConfig.showAttribute( qId, 'jndiName' ) == qcfname:
			print '%s[Waring] : Queue Connetion Factory (%s) already Exist%s'%(YELLOW,qcfname,END)
			if isSkipIfExist == 1:
				echoMessage = '[Warning] : %sDeleting%s Queue Connetion Factory'% (RED,END,qcfname)
				print echoMessage,
				done = AdminTask.deleteWMQConnectionFactory(qcfId)
				print '.' * (100 - len(echoMessage)),
				if done:
					print '[ %sDONE%s ]'%(GREEN,END)
					isExist = 1
				else:
					print '[ %sERROR%s ]'%(RED,END)
					isExist = 0
			else:
				print '[Warning] : %sSkipping%s Queue Connetion Factory  (%s)'% (YELLOW,END,qcfname)
				isExist = 0
				
	if isExist == 1:
		echoMessage = '[Info] : Creating Queue Jndi (%s)'% qcfname
		print echoMessage
		done = AdminTask.createWMQConnectionFactory( scopeID, asAttrs )
		print '.' * (100 - len(echoMessage)),
		if done:
			print '[ %sDONE%s ]'%(GREEN,END)
		else:
			print '[ %sERROR%s ]'%(RED,END)

#-------------------------------------------------------------------------------
# Name: SyncNodes
#-------------------------------------------------------------------------------
def SyncNodes():
	nodes = AdminTask.listNodes()
	for node in nodes.splitlines() :
		if node not in [ 'was_dmgr_node', 'wps_dmgr_node' ] :
			sync = AdminControl.completeObjectName( 'type=NodeSync,node=%s,*' % node )
			if sync == '' :
				print '\nSyncNodes: ERROR --- Unable to synchronise with node %s. Nodeagent appears inactive.' % node
			else :
				if AdminControl.invoke( sync, 'sync' ) == 'true':
					print 'Synchronization successfully with Node %s.' % node
				else :
					print '\nSyncNodes: ERROR --- Unable to synchronise with node %s. Check the logs for more information.' % node
