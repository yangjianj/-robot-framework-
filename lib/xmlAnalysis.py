import xml.etree.ElementTree as ET

def get_result_from_outputxml(outputfile):
    #解析output.xml文件，返回统计结果,suit,cases信息 及通过信息
    result={}
    tree= ET.parse(outputfile)
    root= tree.getroot()
    result['statistics']= get_suite_statistics(root)
    result['suites']= get_suite_test_msg(root)
    return result


def get_suite_test_msg(suite,result=[]):
    #获取xml文件suite,test执行结果信息
    sub_suite= suite.findall('suite')
    if sub_suite == []:
        suite_status = suite.find("status").get("status")
        suite_dic= {"suite_name":suite.get("name"),"suite_source":suite.get("source"),"status":suite_status,"tests":[]}
        tests= suite.findall('test')
        for test in tests:
            test_status= test.find("status").get("status")
            test_dic= {"test_name":test.get("name"),"status":test_status}
            suite_dic["tests"].append(test_dic)
        result.append(suite_dic)
    else:
        for i_suite in sub_suite:
            get_suite_test_msg(i_suite,result)
    return result

def get_suite_statistics(suite):
    #获取xml文件执行统计信息，suite=output_xml.root
    result={}
    statistics= suite.find("statistics")
    total= statistics.find("total")
    stat_list= total.findall("stat")
    for stat in stat_list:
        if stat.text == "All Tests":
            result["passed"] = stat.get("pass")
            result["failed"] = stat.get("fail")
    return result

if __name__ == '__main__':
    re= get_result_from_outputxml('../output/pabot_results/0/output.xml')
    #re= get_result_from_outputxml('../output/output.xml')
    print(re)
    for i in re["suites"]:
        print(i)