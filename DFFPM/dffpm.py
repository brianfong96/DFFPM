import os

class dffpm():
    def __init__(self, root_dir, list_of_dirs, path_to_root=None):
        """
        root_dir: root directory of the generated structure, should already exist and be in the path of the working directory, if not, pass path_to_root
        list_of_dirs: list of dirs to create. It should be of the format ['d1', 'd1/d2', 'd4']
        path_to_root: optional parameter containing the path to root_dir
        """
        self.working_directory = os.getcwd()
        self.root_dir = root_dir
        if path_to_root:
            if not os.path.exists(path_to_root):
                raise dffpm_ex(1)
            self.root_dir = path_to_root

        if not root_dir in self.working_directory:            
            raise dffpm_ex(2)
        self.root_dir = self.get_path_to(root_dir)
        self.rel_to_abs = dict()
        self.populate_list_of_dirs(list_of_dirs)
        print(self.rel_to_abs)
        return

    def populate_list_of_dirs(self, list_of_dirs):
        for dirs in list_of_dirs:
            self.populate(dirs)
        return

    def populate(self, dir_path):
        h, t = os.path.split(dir_path)
        if h != t:
            self.populate(h)        
        self.create_dir_record(dir_path)        
        return
    
    def create_dir_record(self, d):
        abs_d = os.path.join(self.root_dir, d)
        if not os.path.exists(abs_d):
            os.mkdir(abs_d)
        self.rel_to_abs[d] = abs_d
        return
        
    def get_path_to(self, d):
        current = self.working_directory
        prev = str()
        ret_path = os.path.join(current, d)
        # Recursively find d 
        while not os.path.exists(ret_path) and not prev == current:
            prev = current
            current = os.path.split(current)[0]
            ret_path = os.path.join(current, d)
        
        if not prev == current:
            return ret_path
        else:
            raise dffpm_ex(3, d)




class dffpm_ex(Exception):
    def __init__(self, err_code, extra=None):
        if err_code == 1:
            self.msg = "Invalid Root Path"
        elif err_code == 2:
            self.msg = "Root Directory not Found"
        elif err_code == 3:
            self.msg = "Cannot find path to: " + extra
        else:
            self.msg = "Unknown Error"
        return     

if __name__ == "__main__":
    root = "DFFPM"
    list_of_dirs = ['test0', 'test1', os.path.join('test1','test3'), 'test2', 'test2', os.path.join('test1', 'test2', 'test3','test1')]
    dff = dffpm(root, list_of_dirs)
    pass