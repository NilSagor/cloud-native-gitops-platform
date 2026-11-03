```bash

kubectl -n shop scale deploy/product-api --replicas=5
sleep 30
kubectl -n shop get deploy product-api 

```

