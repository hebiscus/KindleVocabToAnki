
function InfoPage() {
  return (
    <div className="sm:mx-20 xl:mx-40 2xl:mx-80 my-6">
      <section className="sm:text-sm xl:text-xl">
        <h1 className="sm:text-lg xl:text-3xl">Instructions, <a className="text-purple-700 underline hover:text-purple-800" href="https://youtu.be/oYFIydvBSEk?si=0G3xYl9ryp1LJUwu">Video tutorial:</a>
        </h1>
        <ol className="list-decimal [&>*]:my-4">
          <li>First you need to get your looked up words out of your Kindle via USB. Fortunately, they’re stored for us at: Kindle/system/vocabulary/vocab.db. If you can’t find it, go to the main Kindle folder and search for vocab.db. It’s hiding somewhere!</li>
          <li>Next, upload the same file on the homepage after clicking “Choose a file” and “Upload”.</li>
          <li>Tadahh! If everything went smoothly (ekhem, my other server didn’t crash) you should see a big purple “Download” button. Click on it and save your words.csv file onto your device. </li>
        </ol>
        <span className="sm:text-base xl:text-2xl">Next comes the Anki part for which we’ll use the file you just downloaded.</span>
        <ol className="list-decimal [&>*]:my-4">
          <li>Open your Anki and go to Tools &gt; Manage Note Types. Depending on the style you wish to pick for your flashcards you’ll need to click “Add”. If you want good old default flashcards pick Add:Basic. </li>
          <li>Give it some name, click on it when it shows up in your list of note types and click “Fields”. </li>
          <li>That’s the place you’re formatting the fields of the notes. Naming doesn’t matter much. Although you must remember it for next step, so it’s best you keep it Word, Context and...</li>
          <li>Add a new field and call it Definition! Don’t forget about saving your changes.</li>
          <li>Next up you have to format the flashcard itself. For that click “Cards”.</li>
          <li>Formatting a card is totally up to you. I’ve went for a simple layout where there’s two sides: Word on the front and Context + Definition on the back. As you can see on the video instructions, to include Definition on the back you need to do this: "{"{{Definition}}"}". All the other styles are simple HTML tags to make it a little prettier. </li>
          <li>Click that save!</li>
          <li>On the main screen of Anki click “Import File” and pick words.csv file you downloaded.</li>
          <li>Here goes the important parts: for field separator choose “Comma”, Allow for HMTL in fields, for the Notetype choose the one you made a minute ago and click “Import”.</li>
          <li>You’ll see a new deck name “Default” with all your flashcards!</li>
        </ol>
      </section>
    </div>
  )
}

export default InfoPage;