## Responsible for keeping track of previous requests done to the system


### TODO:

- [x] Implement all tables and respective CRUDs
  - [x] Implement `search_history` table
    - [x] create (`save_search()`)
    - [x] read (both `find_search_by_term()` and `get_all_history()`)
    - [x] delete
  - [x] Implement `search_results` table
    - [x] create
    - [x] read
    - [x] delete

<br>

---

### Notes:
* did not implement update due to lack of need.
* deleting a record in the `search_history` table triggers a `CASCADE`, automatically removing the corresponding record in `search_results`.

<br>

---

### Current tables:

### `search_history`
Stores the metadata and bounding box coordinates of each search.

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | `INTEGER` | **Primary Key (PK)**. Auto increment. |
| `slug` | `TEXT` | Friendly identifier or search date/time. |
| `lat_tl` | `REAL` | Latitude of the Top-Left point. |
| `lon_tl` | `REAL` | Longitude of the Top-Left point. |
| `lat_br` | `REAL` | Latitude of the Bottom-Right point. |
| `lon_br` | `REAL` | Longitude of the Bottom-Right point. |

<br>

### `search_results`
Stores the mathematical calculations and predictions tied to a specific search.

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | `INTEGER` | **Primary Key (PK)** and **Foreign Key (FK)**. References `search_history(id)`. Ensures the 1:1 relationship. |
| `population` | `INTEGER` | Estimated total number of inhabitants in the area. |
| `population_density` | `REAL` | Calculated population density (inhab/km²). |