class Module:
    def __init__(self, module_id, module_type, version, parameters, mapper=None, metadata=None):
        self.id = module_id
        self.module = module_type
        self.version = version
        self.parameters = parameters
        self.mapper = mapper
        self.metadata = metadata

class Metadata:
    def __init__(self, designer, restore, parameters=None, expect=None):
        self.designer = designer
        self.restore = restore
        self.parameters = parameters
        self.expect = expect

class Designer:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Restore:
    def __init__(self, parameters=None, expect=None):
        self.parameters = parameters
        self.expect = expect

class Parameter:
    def __init__(self, name, param_type, label, required=False, spec=None):
        self.name = name
        self.type = param_type
        self.label = label
        self.required = required
        self.spec = spec

class Flow:
    def __init__(self, modules, routes=None):
        self.modules = modules
        self.routes = routes

class PandaDocToMonday:
    def __init__(self, name, flow, metadata):
        self.name = name
        self.flow = Flow(flow)
        self.metadata = metadata

# Parameters instances
param_pandadoc_hook = Parameter(name="__IMTHOOK__", param_type="hook:pandadoc", label="Webhook", required=True)

# Metadata for module 56
metadata_module_56 = Metadata(
    designer=Designer(x=-347, y=415),
    restore=Restore(parameters={
        "__IMTHOOK__": {
            "data": {"editable": "false"},
            "label": "CheckStatus"
        }
    }),
    parameters=[param_pandadoc_hook]
)

# Module instances
module_56 = Module(
    module_id=56,
    module_type="pandadoc:watchDocuments",
    version=1,
    parameters={"__IMTHOOK__": 1350177},
    mapper={},
    metadata=metadata_module_56
)

# Continue defining other modules similarly

# Define the flow with a list of modules
flow_modules = [module_56]  # Continue adding other modules

# Define the system
panda_doc_to_monday = PandaDocToMonday(
    name="PandaDoc signed Upload to Monday",
    flow=flow_modules,
    metadata=None  # Define metadata if necessary
)