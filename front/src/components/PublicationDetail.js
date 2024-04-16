// src/components/PublicationDetail.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';

const PublicationDetail = ({ match }) => {
  const [publication, setPublication] = useState(null);

  useEffect(() => {
    axios.get(`/api/v1/publications/${match.params.id}/`)
      .then(response => {
        setPublication(response.data);
      })
      .catch(error => {
        console.error('Error fetching publication:', error);
      });
  }, [match.params.id]);

  if (!publication) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>{publication.title}</h2>
      <p>Author: {publication.author}</p>
      <p>{publication.content}</p>
    </div>
  );
};

export default PublicationDetail;
