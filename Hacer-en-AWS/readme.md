Antes de crear el GitHub Action, configura AWS para usar OIDC con GitHub.

    1.  Crea un Proveedor OIDC en AWS:
        Ve a la consola de AWS > IAM > Identity Providers > Add Provider.
        Selecciona OpenID Connect.
        Ingresa:
            Provider URL: https://token.actions.githubusercontent.com
            Audience: sts.amazonaws.com
        Haz clic en Get Thumbprint y luego en Create.
    2.  Crea un Rol de IAM:
        Ve a IAM > Roles > Create Role.
        Selecciona Web Identity y elige el proveedor OIDC que creaste.
        En Trust Relationship, edita el JSON: segun el archivo "Trust_Relationship.json"
        Reemplaza <TU-ACCOUNT-ID> (lo encuentras en "My Account") y <TU-USUARIO> con tu nombre de usuario de GitHub.

    3.  Asigna Permisos al Rol:

        Crea una política personalizada (IAM > Policies > Create Policy) con: "Create_Policy.json"
        Asocia esta política al rol y guárdalo (ej., llámalo GitHubActionsRole)
    4.  Crea Recursos en AWS para Prueba:

        ECR: Crea un repositorio (winempresas-repo) en Elastic Container Registry.
        ECS: Configura un clúster (winempresas-cluster) y un servicio (winempresas-service) con Fargate (puedes hacerlo manualmente por ahora para probar).
