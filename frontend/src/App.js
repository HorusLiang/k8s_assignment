import snameService from './services/sname.js'
import { useState, useEffect } from 'react'



const App=()=> {
  const [snames, setSnames] = useState([])
  useEffect(() => {
    snameService
    .getAll()
    .then(initialSnames => {
      setSnames(initialSnames)
    })
  }, [])

  const handleSend=async(event)=>{
    event.preventDefault()
    const formData = new FormData(event.target)
    const fname = formData.get("fname");
    const lname = formData.get("lname");
    setSnames([...snames, { fname, lname }]);
    await snameService.createNew({ fname, lname });
    event.target.reset();
  }
  return (
    <div>
       <form onSubmit={handleSend}>
          <label for="fname">First name:</label>
          <input type="text" id="fname" name="fname"/>
          <label for="lname">Last name:</label>
          <input type="text" id="lname" name="lname"/>
          <button type="submit">Send</button>
       </form>
       <ul>
        {snames.map(sname => (
          <li>
            {sname.fname} {sname.lname}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
