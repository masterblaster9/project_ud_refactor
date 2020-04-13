## This is development for the kubernetes portion.

## secrets files are mising from this repo - due to secret nature

# env-secrets.yaml

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: env-secret
type: Opaque
data:
  POSTGRESS_USERNAME: <base64>
  POSTGRESS_PASSWORD: <base64>
  JWT_SECRET: <base64>
```

# aws-secrets.yaml

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: aws-secret
type: Opaque
data:
  credentials: WIA... - <base64 encoded file>
```

easy way to generate bas64 encoded strings and decode

```
echo -n <string> | base64
echo -n <string> | base64 --decode
```

# base.py helper for base64 encoding files
