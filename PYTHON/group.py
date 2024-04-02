temp = '''
    <li>
        <h2>$NAME$</h2>
        <img src="" alt="">
        <button class="email">  <a href="$et$">$email$</a></button>
        <p class="topic">$Works$</p>
    </li>
    '''
    
    mailto:john@example.com
dicti = {}    
    
for i in range(int(input("How many? \n"))):
    name = input('Name: \n')
    email = input('email: \n')
    works = input('works: \n')
    mail_to = 'mailto:'+email
    x = temp 
    x = x.replace('$NAME$', name)    
    x = x.replace('$email$', email)    
    x = x.replace('$Works$', works) 
    x = x.replace('$et$',mail_to)


    dicti.update({name:x})