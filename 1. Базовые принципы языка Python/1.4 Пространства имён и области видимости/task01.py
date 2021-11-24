namespaces = {'global': None}
variables = {'global': set()}

n = int(input())
for i in range(n):
    cmd, namespace, variable = input().split()
    if cmd == 'create':
        namespaces[namespace] = variable
        variables[namespace] = set()
    elif cmd == 'add':
        variables[namespace].add(variable)
    else:
        while namespace is not None:
            if variable in variables[namespace]:
                break
            namespace = namespaces[namespace]
        print(namespace)