# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET

# find the element need to index in the xml document
def parseXmlFile(path):
    tree = ET.parse(path)
    root = tree.getroot()
    #  get the title
    title = ''
    for child in root.iter('title'):
        title = child.text
    # get the full_text
    full_text = ''
    for child in root.iter('block'):
        temp = child.get('class')
        if(temp == 'full_text'):
            for temp2 in child.findall('p'):
                full_text = '%s%s%s' % (full_text, ' ', temp2.text)

    # get the doc_id
    for child in root.iter('docdata'):
        doc_id = child.find('doc-id').get('id-string')



    return (title, full_text, doc_id)








if __name__ == '__main__':
    path = 'F:\\BaiduNetdiskDownload\\nyt_corpus_LDC2008T19\\nyt_corpus\\datatest\\test.xml'


    (title, content, id) = parseXmlFile(path)
    print ('------------------------------')
    print (title)
    print ('------------------------------')
    print (content)
    print ('------------------------------')
    print (id)
    print ('------------------------------')
    # tree = ET.parse(path)
    #
    # root = tree.getroot()
    # print  '111111'
    #
    # for neighbor in root.iter('title'):
    #     print  neighbor.attrib
    # print '11111'
    #
    # print ('root is',root.tag,  root.attrib)
    # for neighbor in root:
    #     print (neighbor.tag, neighbor.attrib)
    #
    # sad = root.find('head')
    # print  sad.find('title').text
    # print  'haiyousei!!!!!!!!!!!!!!'
    # for child in sad.findall('meta'):
    #     print (child.get('content'),child.get('name'))
    #
    # for neighbor in root.iter('title'):
    #     print neighbor.attrib
    #
    #
    # for country in root.findall('full_text'):
    #     contentStr = country.find('full_text').text
    #     print contentStr
    #
    # print 'asdfsdafsdafsadfdsaf'
    # bodyPart = root.find('body')
    # for child in root.iter('body.content'):
    #     for temp in child.findall('block'):
    #         class1 = temp.get('class')
    #         print (temp.tag, class1)
    #         if(class1 == 'lead_paragraph'):
    #             print temp.find('p').text
    #
    # print '=============================='
    #
    #
    # for child in root.iter('body.content'):
    #     for qq in child.findall('block'):
    #         name = qq.find('class')
    #         if(name == 'full_text'):
    #             print qq.find('p').text
    #
    # print '===================]'
    # for child in root.iter('block'):
    #     temp = child.get('class')
    #     if(temp == 'full_text'):
    #         print '1'
    #         temp1 = child.find('p')
    #         print temp1.text
    #
    # print '=================='