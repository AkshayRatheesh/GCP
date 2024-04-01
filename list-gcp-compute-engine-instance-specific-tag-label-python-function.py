from google.cloud import compute_v1

def list_instances_with_tag(project_id: str, zone: str, tag: str):
    """
    List instances with a specific tag in the given zone and project.

    Args:
        project_id: Project ID or project number of the Cloud project.
        zone: Name of the zone (e.g., "us-west3-b").
        tag: The tag you want to filter by (e.g., "prod").

    Returns:
        A list of instance names.
    """
    client = compute_v1.InstancesClient()
    instances = client.list(project=project_id, zone=zone)

    filtered_instances = []
    for instance in instances:
        if tag in instance.tags.items:
            filtered_instances.append(instance.name)

    return filtered_instances

# Example usage
project_id = "akshay0007"
zone = "us-west3-b"
tag_to_filter = "http-server"
prod_instances = list_instances_with_tag(project_id, zone, tag_to_filter)

print(f"Instances with '{tag_to_filter}' tag in zone {zone}:")
for instance_name in prod_instances:
    print(f" - {instance_name}")
