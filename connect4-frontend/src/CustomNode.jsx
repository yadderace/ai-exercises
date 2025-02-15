import React from 'react';

const CustomNode = ({ nodeDatum, toggleNode }) => (
  <g>
    <circle r="15" onClick={toggleNode} />
    <text fill="black" strokeWidth="1" x="20">
      {nodeDatum.name}
    </text>
    <foreignObject width="200" height="200" x="20" y="20">
      <div className="tooltip">
        <p>Best Move: {nodeDatum.attributes.best_move}</p>
        <p>Evaluation: {nodeDatum.attributes.evaluation}</p>
        <p>Score: {nodeDatum.attributes.score}</p>
        <p>Min: {nodeDatum.attributes.min}</p>
        <p>Max: {nodeDatum.attributes.max}</p>
      </div>
    </foreignObject>
  </g>
);

export default CustomNode;