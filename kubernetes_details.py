from kubernetes import client, config

# Load Kubernetes configuration
config.load_kube_config()

# Function to get Kubernetes pod logs
def get_pod_logs(pod_name, namespace="default"):
    v1 = client.CoreV1Api()
    pod_name = pod_name.strip()
    try:
        logs = v1.read_namespaced_pod_log(name=pod_name, namespace=namespace)
        return logs
    except client.exceptions.ApiException as e:
        return f"Error: {e.reason}. Details: {e.body}"

# Function to describe a Kubernetes pod
def describe_pod(pod_name, namespace="default"):
    v1 = client.CoreV1Api()
    pod_name = pod_name.strip()
    try:
        pod = v1.read_namespaced_pod(name=pod_name, namespace=namespace)
        return str(pod)
    except client.exceptions.ApiException as e:
        return f"Error: {e.reason}. Details: {e.body}"

# Function to describe a Kubernetes node
def describe_node(node_name):
    v1 = client.CoreV1Api()
    node_name = node_name.strip()
    try:
        node = v1.read_node(name=node_name)
        return str(node)
    except client.exceptions.ApiException as e:
        return f"Error: {e.reason}. Details: {e.body}"
