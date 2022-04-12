import React from 'react'

function TableHeader()  
{
  return (
    <thead>
      <tr>
        <th>Start</th>
        <th>End</th>
      </tr>
    </thead>
  );
}

function TableBody() {
  //return <tbody />

return
<tr key={index}>
  <td>{row.name}</td>
  <td>{row.job}</td>
  <td>
    <button onClick={() => props.removeCharacter(index)}>Delete</button>
  </td>
</tr>


}



function Table (props) {
  return (
    <table>
      <TableHeader />
      <TableBody characterData={props.characterData} removeCharacter={props.removeCharacter} />
    </table>
  );
}


export default Table;
