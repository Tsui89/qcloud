```code
elasticsearch:
  cluster-nodes: {{range $dir := lsdir "/hosts/postgres"}}{{$ip := printf "/hosts/postgres/%s/ip" $dir}}{{getv $ip}}{{end}}:8200

work-order:
  index: k2fuxi_wo
  type: wo
  es-import-ticket: c1c3fad1-1b09-4693-82fe-904541d794a5
  minimum-should-match: 90%

spring:
  datasource:
    name: search-ds
    url: jdbc:mysql://{{range $dir := lsdir "/hosts/mysql"}}{{$ip := printf "/hosts/mysql/%s/ip" $dir}}{{getv $ip}}{{end}}:8306/db_k2fuxi_wo?useSSL=false&useUnicode=true&characterEncoding=utf8
    username: root
    password: passw0rd
    driver-class-name: com.mysql.jdbc.Driver

wo-import-script:
  shell-path: /home/ubuntu/python/woImport.sh

eureka:
  client:
    serviceUrl:
      defaultZone: http://127.0.0.1:8000/eureka/
```

```
window['__API__'] = 'http://{{getv "/host/ip"}}:9000/k2fuxi-search/'
window['__LOGINAPI__'] = 'http://{{getv "/host/ip"}}:9000/k2fuxi-uc/'
window['__CORPUSAPI__'] = 'http://{{getv "/host/ip"}}:9000/k2fuxi-corpus/'
window['__STATISTICSAPI__'] = 'http://{{getv "/host/ip"}}:9000/k2fuxi-statistics/'
```
```
,{
    "key": "service_params",
    "description": "Custom service configuration properties",
    "type": "array",
    "properties": [{***
      "key": "role_name",
      "description": "Custom service the role (role_name) configuration properties",
      "type": "array",
      "properties": [{***
        "key": "param",
        "label": "Role Param",
        "description": "The param for all slave nodes",
        "type": "string",
        "pattern": "^value.+",
        "default": "value1",
        "range": ["value1", "value11"],
        "required": "yes"
      }]
    }]
  }
```

,
    {
      "key": "env",
      "description": "Custom service configuration properties",
      "type": "array",
      "properties": [
        {
          "key": "role_name",
          "description": "Custom service the role (role_name) configuration properties",
          "type": "array",
          "properties": [
            {
              "key": "param",
              "label": "Role Param",
              "description": "The param for all slave nodes",
              "type": "integer",
              "changeable": true,
              "default": "8080",
              "min": 8000,
              "max": 30000,
              "required": "yes"
            }
          ]
        }
      ]
    }