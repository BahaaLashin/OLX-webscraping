

class CreateHTMLTable:
    
    def html_table(self,table_data):

        # get columns
        columns = list(table_data[0].keys())

        # create table 
        table = '<table border>'
        table += '<tr>'
        
        # set headers
        for column in columns:
            table += '<th>'+column+'</th>'
        table += '</tr>'
        
        # set body
        for data in table_data:
            table += '<tr>'
            for item in data.values():
                table += '<td>'+item+'</td>'
            table += '</tr>' 

        table += '</table>'

        return table