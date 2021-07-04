# coding=utf-8

import webbrowser


class handle_color:

    def build_html(self, html_str):
        # 命名生成的html
        GEN_HTML = "test.html"
        # 打开文件，准备写入
        html_new_str = self.build_full_html_str(html_str)
        f = open(GEN_HTML, 'w')

        # 准备相关变量

        # 写入HTML界面中
        message = """
        <html>
        <body>
        <table border = "1" >
        <tr>
        <th>CODE</th>
        <th>LIGHT</th>
        <th>DARK</th>%s
        </tr>
        </table>
        </body>
        </html>
        """ % (html_new_str)

        # 写入文件
        f.write(message)
        # 关闭文件
        f.close()
        # 运行完自动在网页中显示
        webbrowser.open(GEN_HTML, new=1)

    # 构建普通的td表格
    # 0-255 , 0-1
    # style="background: rgba(0, 0, 0, 0.7)"
    def build_normal_td(self, html_td):
        td = '<tr> ' \
             '<td> {} </td> ' \
             '<td style="background: rgba({})" >{}</td> ' \
             '<td style="background: rgba({})" >{}</td> ' \
             '</tr>'.format(html_td[0],
                            self.get_color_str(html_td[3]),
                            html_td[3],
                            self.get_color_str(html_td[8]),
                            html_td[8])
        return td

    # 构建空白的td表格
    def build_empty_td(self, html_td):
        td = ''
        return td

    # 构建合并的td单行
    def build_compose_td(self, html_td):
        td = '<tr><td colspan=3>{}</td></tr>'.format(html_td[0])
        return td

    def build_full_html_str(self, origin_array):
        origin_array = origin_array[2:]
        my_html = ""
        for td_arr in origin_array:
            print(td_arr)
            # 不为空
            if td_arr[0] is None:
                my_html += self.build_empty_td(td_arr)
            else:
                if td_arr[3] is None:
                    my_html += self.build_compose_td(td_arr)
                else:
                    my_html += self.build_normal_td(td_arr)


        return my_html

    # 获取颜色
    def get_color_str(self, html_th):
        split = html_th.split("#")
        new_array = list(filter(self.equal_empty, split))
        if len(new_array) == 1:
            return Hex_to_RGB('#'+new_array[0]) + ',1'
        elif len(new_array) == 2:
            color = Hex_to_RGB('#' +str(new_array[1])) + ',' + str(self.get_alpha(new_array[0]))
            print(color)
            return color
        else:
            return "174,174,174,0.5"

    def get_alpha(self, color):
        return float(int(color.split("%")[0]) / 100)

    def equal_empty(self, s):
        return s != ""

# 16进制颜色格式颜色转换为RGB格式
def Hex_to_RGB(hex):
    r = int(hex[1:3], 16)
    g = int(hex[3:5], 16)
    b = int(hex[5:7], 16)
    rgb = str(r) + ',' + str(g) + ',' + str(b)
    print(rgb)
    return rgb

if __name__ == '__main__':
    color = "#bababa"
    alpha = "10%"
    print(float(int(alpha.split("%")[0]) / 100))
    Hex_to_RGB(color)


