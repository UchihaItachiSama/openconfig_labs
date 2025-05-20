hostname {{ .ShortName }}
username admin privilege 15 secret admin
!
service routing protocols model multi-agent
!
vrf instance MGMT
!
interface Management1
   description oob_management
   vrf MGMT
{{ if .MgmtIPv4Address }}   ip address {{ .MgmtIPv4Address }}/{{ .MgmtIPv4PrefixLength }}{{end}}
{{ if .MgmtIPv6Address }}   ipv6 address {{ .MgmtIPv6Address }}/{{ .MgmtIPv6PrefixLength }}{{end}}
!
{{ if .MgmtIPv4Gateway }}ip route vrf MGMT 0.0.0.0/0 {{ .MgmtIPv4Gateway }}{{end}}
{{ if .MgmtIPv6Gateway }}ipv6 route vrf MGMT ::0/0 {{ .MgmtIPv6Gateway }}{{end}}
!
management security
   ssl profile self-signed
      cipher-list HIGH:!eNULL:!aNULL:!MD5:!ADH:!ANULL
      certificate selfSigned.crt key selfSigned.key
!
management api http-commands
   protocol https ssl profile self-signed
   no shutdown
   !
   vrf MGMT
      no shutdown
!
management api gnmi
   provider eos-native
   transport grpc oob
      vrf MGMT
!
management api netconf
   transport ssh oob
      vrf MGMT
!
management api restconf
   transport https oob
      ssl profile self-signed
      port 5900
      vrf MGMT
!
ip routing
!
end
