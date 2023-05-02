import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';

const search_target_articles = async () => {
  const response = await fetch('/api/search_target_articles');
  const data = await response.json();
  return data;
};

function App() {
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchResults() {
      setLoading(true);
      const target_articles = await search_target_articles();
      setResults(target_articles);
      setLoading(false);
    }
    fetchResults();
  }, []);

  return (
    <div className="container">
      <h1 className="text-center">Articles sur les personnes fortunées</h1>
      {loading ? (
        <div className="text-center">
          <span className="spinner-border" role="status" aria-hidden="true"></span>
          <p>Chargement des articles...</p>
        </div>
      ) : (
        <div className="list-group">
          {results.map((article, index) => (
            <a
              href={article.url}
              target="_blank"
              rel="noopener noreferrer"
              className="list-group-item list-group-item-action"
              key={index}
            >
              {article.title}
            </a>
          ))}
        </div>
      )}
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('app'));
