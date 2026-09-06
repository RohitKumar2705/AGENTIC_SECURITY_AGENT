def analyze_configuration(configuration: dict):
    findings = []

    if configuration.get("tls_enabled") is False:
        findings.append("TLS is disabled, so communication may not be protected.")

    if configuration.get("default_credentials") is True:
        findings.append("Default credentials are enabled")

    if configuration.get("admin_interface_exposed") is True:
        findings.append("admin. interface are exposed")       

    if not findings: 
        findings.append( "No predefined configuration issues were detected." )
    return { "findings": findings }    