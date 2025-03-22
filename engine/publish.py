import os
from db import Session, Scope, Resource, Endpoint

STORAGE_ROOT = "../storage"

def export():
    session = Session()
    scopes = session.query(Scope).all()

    tag_map = {}
    global_endpoints=[]
    global_resources=[]
    
    for scope in scopes:
        tag = scope.tag or "untagged"
        tag_map.setdefault(tag, []).append(scope)

    for tag, scoped_items in tag_map.items():
        tag_dir = os.path.join(STORAGE_ROOT, tag)
        os.makedirs(tag_dir, exist_ok=True)

        tag_resources = []
        tag_endpoints = []

        for scope in scoped_items:
            scope_dir = os.path.join(tag_dir, scope.name)
            os.makedirs(scope_dir, exist_ok=True)

            res_out = []
            end_out = []

            for resource in session.query(Resource).filter_by(domain_id=scope.id).all():
                res_out.append(resource.name)
                tag_resources.append(resource.name)
                global_resources.append(resource.name)

                endpoints = session.query(Endpoint).filter_by(resource_id=resource.id).all()
                for ep in endpoints:
                    end_out.append(ep.name)
                    tag_endpoints.append(ep.name)
                    global_endpoints.append(ep.name)

            with open(os.path.join(scope_dir, "resources.txt"), "w") as f:
                f.write("\n".join(res_out))

            with open(os.path.join(scope_dir, "endpoints.txt"), "w") as f:
                f.write("\n".join(end_out))


        with open(os.path.join(tag_dir, "resources.txt"), "w") as f:
            f.write("\n".join(sorted(set(tag_resources))))

        with open(os.path.join(tag_dir, "endpoints.txt"), "w") as f:
            f.write("\n".join(sorted(set(tag_endpoints))))
    with open(os.path.join(STORAGE_ROOT, "endpoints.txt"), "w") as f:
        f.write("\n".join(sorted(set(global_endpoints))))
    with open(os.path.join(STORAGE_ROOT, "resources.txt"), "w") as f:
        f.write("\n".join(sorted(set(global_resources))))



    print("Export completed.")

if __name__ == "__main__":
    export()