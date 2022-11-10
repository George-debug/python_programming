const canvasElement = document.getElementById("voronoy-canvas");
const textElement = document.getElementById("voronoy-textarea");
const canvas = canvasElement.getContext("2d");
canvas.scale(1, -1);
canvas.translate(0, -canvasElement.height);

colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink"];

const parsePoints = (str) => {
  const points = str
    .split("\n")
    .map((line) => line.trim())
    .filter((line) => line.length > 0)
    .map((line) => line.split(/[ ,]+/).filter(Boolean))
    .map((point) => {
      return {
        x: point[0] ? parseFloat(point[0]) : 0,
        y: point[1] ? parseFloat(point[1]) : 0,
        f: point[2] ? parseInt(point[2]) : 0,
      };
    });

  return points;
};

const circleCircumscribed = (p1, p2, p3) => {
  const x1 = p1.x;
  const y1 = p1.y;
  const x2 = p2.x;
  const y2 = p2.y;
  const x3 = p3.x;
  const y3 = p3.y;

  const a = x2 - x1;
  const b = y2 - y1;
  const c = x3 - x1;
  const d = y3 - y1;

  const e = a * (x1 + x2) + b * (y1 + y2);
  const f = c * (x1 + x3) + d * (y1 + y3);

  const g = 2 * (a * (y3 - y2) - b * (x3 - x2));

  if (g === 0) {
    return null;
  }

  const x = (d * e - b * f) / g;
  const y = (a * f - c * e) / g;

  const dx = x - x1;
  const dy = y - y1;

  const r = Math.sqrt(dx * dx + dy * dy);

  return {
    center: {
      x,
      y,
    },
    radius: r,
  };
};

const equals = (p1, p2) => Math.abs(p1 - p2) < 0.0001;

const pointsInCircle = (circle, points) => {
  const { center, radius } = circle;
  const { x, y } = center;
  const r = radius ** 2;

  for (point of points) {
    const distance = (x - point.x) ** 2 + (y - point.y) ** 2;
    if (distance < r && !equals(distance, r)) {
      console.log(`point in circle (${point.x}, ${point.y})`);
      return true;
    }
  }

  return false;
};

const getTriangles = (points) => {
  const triangles = [];
  for (let i = 0; i < points.length; i++)
    for (let j = i + 1; j < points.length; j++)
      for (let k = j + 1; k < points.length; k++) {
        circle = circleCircumscribed(points[i], points[j], points[k]);

        if (circle != null && !pointsInCircle(circle, points)) {
          triangles.push([i, j, k]);
        } else {
          console.log(
            `triangle (${points[i].x}, ${points[i].y}) (${points[j].x}, ${points[j].y}) (${points[k].x}, ${points[k].y})`
          );
          console.log(null);
        }
      }

  return triangles;
};

const drawPerpendicular = (p1, p2, circleCenter) => {
  if (p1.f === p2.f) return;
  middleX = (p1.x + p2.x) / 2;
  middleY = (p1.y + p2.y) / 2;

  canvas.beginPath();
  canvas.moveTo(middleX, middleY);
  canvas.lineTo(circleCenter.x, circleCenter.y);
  canvas.stroke();
};

const submitHandler = () => {
  canvas.clearRect(0, 0, canvasElement.width, canvasElement.height);
  const points = parsePoints(textElement.value);
  console.log(points);

  if (points.length === 0) {
    return;
  }

  const minX = Math.min(...points.map((p) => p.x));
  const maxX = Math.max(...points.map((p) => p.x));
  const minY = Math.min(...points.map((p) => p.y));
  const maxY = Math.max(...points.map((p) => p.y));

  const max_val = Math.max(maxX, maxY);
  const min_val = Math.min(minX, minY);
  const delta = max_val - min_val;
  console.log("delta", delta);
  const real_delta = Math.max(canvasElement.width, canvasElement.height);

  const scale = real_delta / delta / 1.5;
  console.log("scale", scale);
  canvas.scale(scale, scale);
  const offsetX = -minX + (real_delta / scale - (maxX - minX)) / 2;
  const offsetY = -minY + (real_delta / scale - (maxY - minY)) / 2;
  console.log("offset", offsetX, offsetY);
  canvas.translate(offsetX, offsetY);

  const triangles = getTriangles(points);

  canvas.lineWidth = 0.01;
  for (triangle of triangles) {
    const [i, j, k] = triangle;
    const p1 = points[i];
    const p2 = points[j];
    const p3 = points[k];

    if (p1.f === p2.f && p2.f === p3.f) continue;
    canvas.strokeStyle = "lightgray";
    canvas.beginPath();
    canvas.moveTo(p1.x, p1.y);
    canvas.lineTo(p2.x, p2.y);
    canvas.lineTo(p3.x, p3.y);
    canvas.lineTo(p1.x, p1.y);
    canvas.stroke();

    canvas.strokeStyle = "black";
    const { center, __radius } = circleCircumscribed(p1, p2, p3);
    drawPerpendicular(p1, p2, center);
    drawPerpendicular(p2, p3, center);
    drawPerpendicular(p3, p1, center);
  }

  for (let i = 0; i < points.length; i++) {
    const p = points[i];
    canvas.beginPath();
    canvas.arc(p.x, p.y, 0.08, 0, 2 * Math.PI);
    canvas.fillStyle = colors[p.f % colors.length];
    canvas.fill();
  }
};
