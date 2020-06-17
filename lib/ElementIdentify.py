class ElementIdentify():
    def __init__(self):
        self.pageyml = 'basedir//ui.yml'
        self.pagedata = None

    def load_yml(self,filepath):
        self.pageyml = filepath
        try:
            pagefile=open(filepath, 'r', encoding="utf-8")
            _page_message = pagefile.read()
            pagefile.close()
            self.pagedata=yaml.load(_page_message)
        except Exception as e:
            self.logger.error('load element yaml file failed')
            self.logger.error(e)

    def locate_element(self,element,page=None):
        if page == '' or page == None:
            page = self.curr_page
        elif page != self.curr_page:
            self.curr_page = page
        if page == None:
            raise Exception('page is None !')
        type = self.pagedata[page][element]["type"]
        value = self.pagedata[page][element]["value"]
        return [type, value]

    def identify_element(self,element,page):
        pass
        
