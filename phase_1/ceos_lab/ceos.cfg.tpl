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
   ssl profile eAPI
      cipher-list HIGH:!eNULL:!aNULL:!MD5:!ADH:!ANULL
      certificate eAPI.crt key eAPI.key
   ssl profile restconf
      certificate restconf.crt key restconf.key
!
management api http-commands
   protocol https ssl profile eAPI
   no shutdown
   !
   vrf MGMT
      no shutdown
!
management api gnmi
   transport grpc oob
      vrf MGMT
!
management api netconf
   transport ssh oob
      vrf MGMT
!
management api restconf
   transport https oob
      ssl profile restconf
      port 5900
      vrf MGMT
!
ip routing
!
end
