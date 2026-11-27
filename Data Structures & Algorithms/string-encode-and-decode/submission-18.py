class Solution:
    # prefix length encoding
    def encode(self, strs: List[str]) -> str:
        ret_str = ""
        for s in strs:
            ret_str += f"{len(s)}#{s}"
        return ret_str

    def decode(self, s: str) -> List[str]:
        list_return = []
        len_flag = True
        len_str = ""
        cur_str = ""
        idx_cur = 0

        for c in s:
            if len_flag:
                if c != "#":
                    len_str += c
                else:
                    len_str_len = int(len_str)
                    if len_str_len == 0:
                        list_return.append("")
                    else:
                        len_flag = False
                    len_str = ""
                        
            else:
                if idx_cur < len_str_len:
                    cur_str += c
                    idx_cur += 1
                    if idx_cur == len_str_len:
                        idx_cur = 0
                        list_return.append(cur_str)
                        cur_str = ""
                        len_flag = True
        return list_return