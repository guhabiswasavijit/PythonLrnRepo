import kebernetesAdmin as admin

output = admin._execute_cmd('kubectl get nodes -o JSON')
print(output)