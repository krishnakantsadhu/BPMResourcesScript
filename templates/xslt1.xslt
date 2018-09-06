<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xsd="http://www.w3.org/2001/XMLSchema" >
    <xsl:template match="READ_WRITE_REQ_IN_GBO">
        <xsl:value-of  select="@name"/>  <xsl:value-of  select="@type"/>
    </xsl:template>    
</xsl:stylesheet>
