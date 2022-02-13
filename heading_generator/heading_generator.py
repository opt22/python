def heading_generator(title, heading_type):
    """heading_generator( 'Greeting', '1')
    <h1>Greeting</h1>
    """
    return f"<h{heading_type}>{title}</h{heading_type}>"
print (heading_generator('Greeting', '1'))
    

def heading_generator2(title, heading_type):
    heading = '<h' + str(heading_type) + ">" + str(title) +'</h' +str(heading_type) + '>'
    return heading

print (heading_generator2('Greeting', '1'))
    



