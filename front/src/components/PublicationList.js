// PublicationList.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function PublicationList({ filterParams }) {
  const [publications, setPublications] = useState([]);

  useEffect(() => {
    const params = new URLSearchParams(filterParams).toString();
    axios.get(`http://127.0.0.1:8000/api/v1/PublicationViewSet/?${params}`)
      .then(response => {
        setPublications(response.data);
      })
      .catch(error => console.error(error));
  }, [filterParams]);

  return (
    <table className="PublicationTable">
      <thead>
        <tr>
          <th>No.</th>
          <th>Публикация</th>
          <th>Статус</th>
          <th>Citations</th>
        </tr>
      </thead>
      <tbody>
        {publications.map((publication, index) => (
          <tr key={publication.id}>
            <td>{index + 1}</td>
            <td className="PublicationCell">
              <a href="src/components/PublicationList#" className="PublicationTitle">{publication.title}</a>
              <p className="PublicationAuthor">Автор:{publication.authors.join(', ')} Журнал: {publication.journal ? publication.journal.name : ''}</p>
              <p>{publication.content}</p>
              <p>Types: {publication.types ? publication.types.map(type => type.name).join(', ') : ''}</p>
            </td>
            <td>
              <span className={`VerifiedStatus ${publication.is_verified ? 'Yes' : 'No'}`}>
                {publication.is_verified ? 'Подтвержден' : 'Не подтвержден'}
              </span>
            </td>
            <td>{publication.citation_count}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default PublicationList;
