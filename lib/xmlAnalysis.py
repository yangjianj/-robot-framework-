import xml.etree.ElementTree as ET


def get_result_from_outputxml(outputfile):
    #解析output.xml文件，返回suit,cases信息 及通过信息
    tree= ET.parse(file=outputfile)

    return 1

if __name__ == '__main__':
    get_result_from_outputxml('')