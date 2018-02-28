class Solution:
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        add = IP.split('.')
        if len(add) == 4: #ipv4 part
            for part in add:
                if part == '': return "Neither"
                for word in part:
                    if word >= '0' and word <= '9':
                        continue
                    return "Neither"
                if part == str(int(part)) and int(part) >= 0 and int(part) <= 255:
                    continue
                else:
                    return "Neither"
            return "IPv4"
        
        add = IP.split(':')
        if len(add) == 8: #ipv6 part
            for part in add:
                if part == '': return "Neither"
                if len(part) <= 4:
                    for word in part:
                        if (word >= '0' and word <= '9') or (word >= 'a' and 
                           word <= 'f') or (word >= 'A' and word <= 'F'):
                            continue
                        return "Neither"
                    continue
                return "Neither"
            return "IPv6"
        return "Neither"