class Solution:

    class TrieNode:
        def __init__(self):
            self.is_end_of_folder = False
            self.children = {}

    def __init__(self):
        self.root = self.TrieNode()

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        for path in folder:

            cur_node = self.root
            sub_paths = path.split('/')

            for sub_path in sub_paths:

                if sub_path == "": continue

                if sub_path not in cur_node.children:
                    cur_node.children[sub_path] = self.TrieNode()
                
                cur_node = cur_node.children[sub_path]

            cur_node.is_end_of_folder = True

        ret = []

        for path in folder:

            cur_node = self.root
            sub_paths = path.split('/')
            is_sub_folder = False

            for sub_path in sub_paths[:-1]:

                if sub_path == "": continue

                next = cur_node.children[sub_path]

                if next.is_end_of_folder:
                    is_sub_folder = True
                    break
                
                cur_node = next

            if not is_sub_folder: ret.append(path)

        return ret

        