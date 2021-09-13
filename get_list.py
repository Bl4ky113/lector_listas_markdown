import os

def searchParentInNestedObj (nested_obj, parent_key, parent_identation, index_path = ""): # DeezNest Objs
  hiking_obj = None
  if isinstance(nested_obj, dict):
    for id, value in nested_obj.items():
      if id == parent_key and nested_obj[id]["identation"] == parent_identation:
        parent_obj = value
        return parent_obj
      if isinstance(value, dict) and id != "parent":
        hiking_obj = searchParentInNestedObj(value, parent_key, parent_identation, index_path + f"['{id}']")
    return hiking_obj

def getListData (list_name, extension):
  file_obj = {}

  file_obj["path"] = os.getcwd() + f"\\lists\\{list_name}{extension}"
  file_obj["exists"] = os.path.isfile(file_obj["path"])
  if file_obj["exists"]:
    file = open(file_obj["path"], "r+t")

    file_obj["tasks"] = {}
    tasks_identations = {}
    for line in file:
      if "- [ ]" in line or "- [x]" in line:
        task_obj = {
          "status": False,
          "label": "",
          "identation": 0,
          "parent": {
            "id": "base",
            "identation": "base"
          },
          "subtasks": {}
        }

        if "- [x]" in line: 
          task_obj["status"] = True
        task_obj["label"] = line.replace("- [ ]", "").replace("- [x]", "").replace("\n", "").strip()
        task_obj["identation"] = line.count(" ", 0, line.index("-"))
        
        if task_obj["identation"] not in tasks_identations.keys():
          tasks_identations[task_obj["identation"]] = 0
        else:
          tasks_identations[task_obj["identation"]] += 1

        if task_obj["identation"] != 0:
          id_parent_task = list(tasks_identations.values())[list(tasks_identations.keys()).index(task_obj["identation"]) - 1]
          identation_parent_task = list(tasks_identations.keys())[list(tasks_identations.keys()).index(task_obj["identation"]) - 1]
          task_obj["parent"]["id"] = id_parent_task
          task_obj["parent"]["identation"] = identation_parent_task

          id_task = tasks_identations[task_obj["identation"]]

          parent = searchParentInNestedObj(file_obj["tasks"], id_parent_task, identation_parent_task)
          parent["subtasks"][id_task] = task_obj
        else:
          id_task = tasks_identations[task_obj["identation"]]
          file_obj["tasks"][id_task] = task_obj

    file.close()
  return file_obj