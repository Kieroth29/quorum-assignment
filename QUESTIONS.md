# Questions

- 1. Discuss your strategy and decisions implementing the application. Please, consider time
     complexity, effort cost, technologies used and any other variable that you understand
     important on your development process.

> I chose FastAPI for this assignment due to the time constraints, as it is a framework that allows for rapid implementation and has fewer structural restrictions. This consideration also influenced my choice of Next.js and the TanStack Table library. The strategy involved extracting CSV data using Pandas and inserting it into Pydantic schemas for normalization, while simplifying the instantiation process and improving typing visibility. I attempted to implement Tailwind to enhance the design but couldn't complete it within the given time frame.

- 2. How would you change your solution to account for future columns that might be
     requested, such as “Bill Voted On Date” or “Co-Sponsors”?

> Update the backend data retrieval functions and schemas to include these columns,
> and modify the frontend components to show the new data or expanding the detail view for each item.

- 3. How would you change your solution if instead of receiving CSVs of data, you were given a
     list of legislators or bills that you should generate a CSV for?

> I would use Pandas for data handling by converting the lists into DataFrames, and then invoke the **to_csv** method.

- 4. How long did you spend working on the assignment?

> 2h57min, most of that was spent on frontend.
